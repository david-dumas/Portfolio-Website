from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
from flask_wtf import validators
 
class ContactForm(Form):
  name = TextField("Naam")
  email = TextField("Email")
  subject = TextField("Onderwerp")
  message = TextAreaField("Bericht")
  submit = SubmitField("Versturen")