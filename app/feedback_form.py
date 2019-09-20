from flask_wtf import FlaskForm
# get the fields
from wtforms import TextField, TextAreaField, SubmitField, StringField, PasswordField, BooleanField
#validation tools
from wtforms import validators, ValidationError
class ContactForm(FlaskForm):
	name = TextField("Name", [validators.Required("Please enter your name.")])
	email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("A valid email address is needed")])
	subject = TextField("Subject", [validators.Required("Please give your feedback a subject.")])
	message = TextAreaField("Message", [validators.Required("Please enter your message.")])
	submit = SubmitField("Send")








