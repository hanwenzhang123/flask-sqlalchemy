#lunch.py
#Add a new view at /today that shows the current user's lunch order for today. It should render the "today.html" template. 

from flask import Flask, g, render_template, flash, redirect, url_for
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, current_user, login_required, logout_user

import forms
import models

app = Flask(__name__)
app.secret_key = 'this is our super secret key. do not share it with anyone!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


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
    g.user = current_user
    

@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        models.User.new(
            email=form.email.data,
            password=form.password.data
        )
        flash("Thanks for registering!") 
    return render_template('register.html', form=form)
  

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.SignUpInForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(
                models.User.email == form.email.data
            )
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You're now logged in!")
            else:
                flash("No user with that email/password combo")
        except models.DoesNotExist:
              flash("No user with that email/password combo")
    return render_template('register.html', form=form)

@app.route('/secret')
@login_required
def secret():
    return "I should only be visible to logged-in users"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
  
  
  
#templates/today.html
#Update templates/today.html to show today's order's date and the order attribute from the order variable. 
#Use strftime on the date with the format %Y-%m-%d.
#Now add a <a> with an href attribute that points to the url for the cancel_order view. 
#The view takes one argument, order_id, which should be the id attribute of the order.

{% extends "layout.html" %}

{% block content %}
<h1>Your lunch for today</h1>

<h2>{{order.date.strftime('%Y-%m-%d %H:%M:%S')}}</h2>
<p>{{order.order}}</p>
<a href="{{ url_for('cancel_order',order_id=order.id) }}">cancel_order</a>
<!-- button to the route for cancel_order with order_id=order.id -->
{% endblock %}
  
