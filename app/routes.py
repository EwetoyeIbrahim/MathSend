from app import app
from flask import render_template, request, redirect, url_for,  flash, Response, jsonify, session, abort
import requests, json, urllib.parse
from random import randint
from app.mathsend_engine import human_math as calcEngine
from app.helpTxt import helpTopics
from app.quotes import quotes
from app.feedback_form import ContactForm
from flask_mail import Message, Mail
import telepot
from multiprocessing import Value
import requests

teleg_bot = telepot.Bot(app.config["TG_TOKEN"])
#facebook related
fbToken = app.config["FB_ACCESS_TOKEN"]
webhookSetupToken = app.config["FB_SETUP_CHALLENGE"]
#mail Initializations
mail = Mail()
mail.init_app(app)
sender = app.config["MAIL_USERNAME"]
recipient = app.config["RECIPIENT"]
backend_stat = app.config["STAT_SECREAT"]



@app.route("/", methods=["GET"])
def home():
    expression = session.get('expression', None)
    if expression:
        recent = api_compute(expression)
    else:
        pick = randint(0,len(quotes)-1)
        recent = {"ques":"", "answ":"",
                  "quote":quotes[pick], "ads_val": pick%2,
                  "link": "",
                  "stat": {"overall_count": stat_format(api_compute.counter)},
        }
    return render_template("index_template.html",recent = recent),200

@app.route("/question", methods=["GET"])
def web_solution():
    in_expr = request.query_string.decode("utf-8")
    session['expression'] = urllib.parse.unquote(in_expr)
    #result = home(urllib.parse.unquote(in_expr))
    return redirect(url_for('home'))

@app.route("/api/v1.0/compute", methods=["GET"])
def api_compute_call():
    question = make_question(request.query_string.decode("utf-8"))
    result = api_compute(question)
    api_call.counter +=1
    return jsonify(result)

@app.route("/api/v1.0/rewrite", methods=["GET"])
def api_rewrite_call():
    api_call.counter +=1
    question = make_question(request.query_string.decode("utf-8"))
    message = calcEngine.rewrite(question)
    pick = randint(0,len(quotes)-1)
    quote = quotes[pick]
    result = {"ques":in_expr,
              "answ":message,
              "quote":quote,
              "stat": {"overall_count": web_solution.counter +
                       api_call.counter + fb_webhook.counter +
                       telegram_webhook.counter
                       }
              }
    return jsonify(result)

def api_compute(in_expr):
    api_compute.counter+=1
    message = calcEngine.compute(in_expr)
    pick = randint(0,len(quotes)-1)
    quote = quotes[pick]
    recent = {"ques":in_expr,
              "answ":message,
              "quote":quote,
              "link": "www.mathsend.com/question?"+ in_expr,
              "stat": {"overall_count": web_solution.counter +
                       api_call.counter + fb_webhook.counter +
                       telegram_webhook.counter
                       }
              }
    return recent

@app.route("/api/"+backend_stat, methods=["GET"])
def api_call():
    api_call.counter +=1
    result = {"stat": {"overall_count": api_compute.counter,
                       "website_count" : web_solution.counter,
                       "external_api_call" : api_call.counter,
                       "facebook_calls" : fb_webhook.counter,
                       "telegram_count": telegram_webhook.counter
                       }
              }
    return jsonify(result)


@app.route("/<string:in_expr>", methods=["GET"])
# I want to preserverve the previous method, /2*89
# but I want redirect them to the new form /question?2*89
def solved(in_expr):
    return redirect("question?"+ in_expr)



@app.route("/advertise") #to override the format of help text for social media
def advert():
    return render_template("advert.html")
@app.route("/privacy")
def privacy():
    return render_template("MATHSEND_Privacy.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender= sender, recipients=recipient.split())
      msg.body = """
      From: %s &lt;%s&gt;
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)

      return render_template('contact.html', success=True)

  elif request.method == 'GET':
    return render_template('contact.html', form=form)

@app.route("/Simplifications", methods=["GET"])
def simplifications():
    return render_template('Simplifications.html')

@app.route("/Calculus", methods=["GET"])
def Calculus():
    return render_template('Calculus.html')

@app.route("/Solve", methods=["GET"])
def Solve():
    return render_template('Solve.html')

@app.route("/help", methods=["GET"])
def forum_home():
    house= helpTopics
    return render_template("help.html", **locals())

# Telegam webhook, not assesible to anyuser
@app.route("/mathsend_telegram_webhook",methods=["GET","POST"])
def telegram_webhook():
    telegram_webhook.counter +=1
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        message = api_compute(text)["answ"]
        teleg_bot.sendMessage(chat_id, message)
        return "Success", 200

@app.route('/facebook_messenger_hook', methods=['GET'])
def verify():
    # our endpoint echos back the 'hub.challenge' value specified when we setup the webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == webhookSetupToken:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

@app.route('/facebook_messenger_hook', methods=['POST'])
def fb_webhook():
    fb_webhook.counter += 1
    data = json.loads(request.data.decode('utf-8'))
    for entry in data['entry']:
        user_message = entry['messaging'][0]['message']['text']
        user_id = entry['messaging'][0]['sender']['id']
        data = {
            'recipient': {'id': user_id},
            'message': {}
        }
        ansed = api_compute(user_message)["answ"]
        data['message']['text'] = ansed
        requests.post(
            'https://graph.facebook.com/v2.6/me/messages/?access_token=' + fbToken, json=data
            )
    return Response(response="EVENT RECEIVED",status=200)


@app.errorhandler(404)
def not_found_error(error):
    return Response(response="""
                    404: It seems you took a wrong turn, Kindly start from <a href ='/'>Mathsend.com</a>
                    """, status=404)

def stat_format(num_val):
    num_val = float('{:.3g}'.format(num_val))
    magnitude = 0
    while abs(num_val) >= 1000:
        magnitude += 1
        num_val /= 1000.0
    return '{}{}'.format('{:f}'.format(num_val).rstrip('0').rstrip('.'),['',' Thousand',' Million',' Billion',' Trillion',' Quadrillion',' Quintillion', ' Sextillion', ' Septillion'][magnitude])

api_compute.counter = 263976     # overall count
web_solution.counter = 250407   # web count 14/09/2019
api_call.counter = 618          # explicit api call
fb_webhook.counter = 2947       # facebook count
telegram_webhook.counter= 10004 # telegram count

def make_question(in_expr):
    question = urllib.parse.unquote(in_expr)
    try:
        if question[0]=="=":
            # curl needs an = sign to work effectively
            question = question[1:]
    except:
        abort(500)
    return question

if __name__ == "__main__":
    app.run(debug=True, processes=8)
    r = requests.get('https://www.python.org')
    print(r.status_code) 