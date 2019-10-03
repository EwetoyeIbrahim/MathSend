from . import info_text

my_texts = {
    "help" :	info_text.helptxt,
    "hi": 		"Hi, give me your mathematical expression",
    " " : 		"hi",
    "@mathsend_bot":	"hi",
	"mathsend_bot":  	"hi",
	"@mathsend": 		"hi",
	"mathsend": 		"hi",
    "about" :	info_text.abouttxt,
    "errortxt" :info_text.errortxt,
    "" : 		"Hi",
	"start" : 	"Welcome, Please supply your mathermatical expression"
}

def norm_input(expression):
	words = {
		'^': 				'**',
	    'inf': 				'oo',
	    '@mathsend_bot':	' ',
	    'mathsend_bot':  	' ',
	    '@mathsend': 		' ',
	    'mathsend': 		' ',
		'plus':				'+',
		'minus':			'-',
		'times':			'*',
		'multiply by':		'*',
		'divide':			'/',
		'div':				'/',
		'divide by':		'/',
		'differentiate':	'diff',
		'divided by':		'/',
		'trigsimplify': 	'trigsimp',
		'trigexpand': 		'hyperexpand'
  }

	for key in words:
		if (key in expression):
			expression = expression.replace(key,words[key])
	return expression

