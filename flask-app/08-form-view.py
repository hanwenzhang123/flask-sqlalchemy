form.validate_on_submit() - When the form is submitted through POST, make sure the data is valid.
Macro - A custom, executable bit of templating.
form.hidden_tag() - Renders hidden fields inside of a hidden <div>

{% macro %} - A function in a template to repeat code on demand. Often really useful for things like form fields.

If you're constantly getting a locked database, change your User.create_user method to the following:

@classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            with DATABASE.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password),
                    is_admin=admin)
        except IntegrityError:
            raise ValueError("User already exists")
            
login_user - Function to log a user in and set the appropriate cookie so they'll be considered authenticated by Flask-Login


#Add a new view to lunch.py. The function name should be register and the route should be "/register". 
#It should accept both GET and POST methods. For now, have it return the string "register".

#Your register() view needs to create an instance of the SignUpForm from forms. 
##It should also render and return the register.html template, import render_template. 
#In the template's context, name the SignUpForm instance as form.

#update the register() view so that the form is validated on submission. 
#If it's valid, use the models.User.new() method to create a new User from the form data and flash the message "Thanks for registering!". You'll need to import flash().

from flask import (Flask, render_template, flash, g)
from flask.ext.login import LoginManager

 

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.select().where(
            models.User.id == int(userid)
        ).get()
    except models.DoesNotExist:
        return None


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()
    

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.SignUpForm()
    if form.validate_on_submit():
        models.User.new(form.email.data, form.password.data)
        flash("Thanks for registering!")
    return render_template('register.html', form=form)
