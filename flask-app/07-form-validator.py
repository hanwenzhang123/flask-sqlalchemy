pip install flask-wtf

common ones:
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                               Length, EqualTo)
                               
Flask-WTF uses wtforms behind the scenes for the actual form, field, and widget creation.


#exercise

#Create a new Form class named SignUpForm. Give it two fields, email and password. 
#email should be a StringField and password should be a PasswordField.

#Add DataRequired and Email to the validators for the email field.
#add DataRequired and Length to the validators for password. Set the min for Length to 8.

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import (DataRequired, Email, Length)

class SignUpForm(Form):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=8)])
