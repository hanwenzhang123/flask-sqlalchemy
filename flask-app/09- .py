Use flask_login instead of flask.ext.login

logout_user() - Method to remove a user's session and sign them out.
@login_required - Decorator to mark a view as requiring a user to be logged in before they can access the view.



#Currently, "/secret" isn't protected from anonymous users. 
#Mark it so it requires users to be logged in. You'll need to import login_required.

#Now add a view named logout() with "/logout" as its route. This view should log the user out and then redirect to "/login". 
#You'll need to import logout_user, redirect, and probably url_for.

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
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
