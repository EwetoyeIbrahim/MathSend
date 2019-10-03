# **MathSend**

Contents:
* [MathSend Web](#MathSend-Web)
* [MathSend API](#MathSend-API)
  * [Approach](##Simple-Approach)
  * [Endpoints (by examples)](##Two-endpoints-are-provided-in-the-API:-compute-and-rewrite)
  * [Features](##Features)
  * [Conclusion](##Conclusion)

---
## **MathSend Web**
MathSend is a mathematics solving chat-bot. Its aim is to solve one-line mathematical expressions through chat messages.  
It can be accessed through three means:
* [online](https://www.mathsend.com) at https://www.mathsend.com;
* on [Telegram](https://t.me/MATHSEND_bot) at https://t.me/MATHSEND_bot;
* on [Facebook messenger](https://www.facebook.com/mathsend.bot) at https://www.facebook.com/mathsend.bot
___
---




## **MathSend API**
This tutorial will be a very short tutorial. Now programmers do not have to waste time figuring out how to handle mathematical expressions as they can now let Mathsend API handle that while they face other important areas. It is the online version of the yet to be released Human math python wrapper which I built to serve Mathsend chat bot. In *3 minutes* from now, you will able to use the API
___


___

### **Simple Approach**
Programmers from any language of simply concatenate the API url ```http://mathsend.com/api/v1.0/compute?```
with the desired problem, say ```differentiate(2x+2sin(5x))```, to return a JSON output.

>URL  
[http://mathsend.com/api/v1.0/compute?differentiate(2x+2sin(5x))](http://mathsend.com/api/v1.0/compute?differentiate(2x+2sin(5x)))


### **Two endpoints are provided in the API: *compute* and *rewrite***  
I guess they are best illustrated by example.

#### Mathsend Request Examples:
1. To get a compute a human readable mathematical expression, say integrate(3x^4+2sin(5x)), we have:

    * From a browser:  
        >[http://mathsend.com/api/v1.0/compute?integrate(3x^4+2sin(5x))](http://mathsend.com/api/v1.0/compute?integrate(3x^4+2sin(5x)))
    * For curl:
        >```curl -L GET http://mathsend.com/api/v1.0/compute?=integrate(3x^4+2sin(5x))```

    * For Python:
        >```from urllib import request```
        >
        >```response = request.urlopen(“http://mathsend.com/api/v1.0/compute?integrate(3x^4+2sin(5x))”).read()```

2. To get rewrite an expression in python recognisable format without solving, use the rewrite in place of compute, for example, to rewrite x^2=+7sin(5x)+6x we have:
    * From a browser: 
        >[http://mathsend.com/api/v1.0/rewrite?x^2=7sin(5x)+6x](http://mathsend.com/api/v1.0/rewrite?x^2=7sin(5x)+6x)

    * For curl:
        >```curl -L GET http://mathsend.com/api/v1.0/rewrite?=x^2=7sin(5x)+6x```

    * For Python:
        >```from urllib import request```
        >
        >```response = request.urlopen(“http://mathsend.com/api/v1.0/rewrite?x^2=7sin(5x)+6x”).read()```

#### Mathsend API Response:
It returns a JSON response which contains four attribute: The question itself (ques), solution to the question (answer); a Mathematics quote; and the overall number of mathematical computations carried out by the  app based on several source (stat) which are telegram, facebook messenger, website use, and direct API call which we are discussing about.

>Reponse  
>```
>{
>  "answ": "3*x^5/5 - 2*cos(5*x)/5", 
>  "ques": "integrate(3x^4+2sin(5x))", 
>  "quote": "Mathematics is a hard thing to love. It has the unfortunate habit, like a rude dog, of turning its most unfavourable side towards you when you frst make contact with it.  -- David Whiteland", 
>  "stat": {
>    "overall_count": 57003
>  }
>}
>```
Obviously, most times one may only need the first value, the solution.

For a dynamic input, we can write a simple script. For example, using Python, one may come up with something like:
```
from urllib import request
def Solve(question):
    link="http://mathsend.com/api/v1.0/compute?"+question
    response = request.urlopen(link).read()
    if response["answ"]:
        return response["answ"]
    return "Something is wrong"

```
### **Features**
Save disk space: As you will get to realize when you are used to the API, for most symbolic computations, may not need to install external library as the API is built upon Sympy and it can accept most expressions you can execute with sympy in a single line, thus Mathsend saves space.

Stateless: Because Mathsend is stateless, you will have to always reconstruct the api url for every line that requires computations that’s where the function like the one above come to play.

Human-like expression: In addition to the functions supported by Sympy module, Mathsend allows for more english-like versions of mathematical functions like differentiate, trigsimplify, and trigexpand. Kindly read the [help page](www.mathsend.com/help) for a brief explanation. You can also consult Sympy library documentation to know more about its operations.

### **Conclusion**
If you are good to use Mathsend provided two conditions are satisfied:
1. You not aiming at executing non-text mathematics, such       as graphs and the likes.
2. You are online
3. Your “massive computation” can be broken down into one mathematical expression at a time.

If above stated conditions are not satisfied, it may be time to look out for alternatives.

(01/10/2019)  
Happy Independence Day, Nigeria.

EWETOYE, Ibrahim  
EwetoyeIbrahim.github.io


