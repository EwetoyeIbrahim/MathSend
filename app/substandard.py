from app import info_text


my_texts = {
	"help" : info_text.helptxt, " " : "hi",
"	mathradbot":"Hello, you need to solve?", "about":info_text.abouttxt,
	"errortxt": info_text.errortxt, "mathsend" : "Hi",
	"start" : "Welcome, are you ready for computation",
	"yes" : "give me your mathematical expression",
	"no" : "Okay, no problem"
}

def norm_input(expression):
	words = {
		'^': 			'**',
	    'inf': 			'oo',
	    '@mathrad_bot':	' ',
	    'mathrad_bot':  ' ',
	    '@mathrad': 	' ',
	    'mathrad': 		' ',
		'plus':			'+',
		'minus':		'-',
		'times':		'*',
		'multiply by':	'*',
		'divide':		'/',
		'div':'/',
		'divide by':	'/',
		'differentiate': 'diff',
		'divided by':	'/',
		'trigsimplify': 'trigsimp',
		'trigexpand': 'hyperexpand',

	}

	for key in words:
		if (key in expression):
			expression = expression.replace(key,words[key])
	return expression
