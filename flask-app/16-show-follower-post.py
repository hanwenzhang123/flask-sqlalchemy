<< - Query operator that works as an equivalent to Python's in keyword.

    def get_stream(self):
        return Post.select().where(
            (Post.user << self.following()) |
            (Post.user == self)
        )

@app.route('/post/<int:post_id>')
def view_post(post_id):
    posts = models.Post.select().where(models.Post.id == post_id)
    return render_template('stream.html', stream=posts)

  
#Update templates/profile.html so that it shows the total number of lunches ordered, followers, and people followed by a user.
  
  {% extends "layout.html" %}
{% from "macro.html" import hide_email %}

{% block content %}

<h1>{{ hide_email(user) }}</h1>

<dl>
    <dd><!-- total  of lunches ordered -->{{ user.orders.count() }}</dd>

    <dd><!--  of followers. user.followers is a queryset of followers -->{{ user.followers.count() }}</dd>

    <dd><!--  of users followed. user.following is a queryset of users followed -->{{ user.following.count() }}</dd>
</dl>

{% endblock %}




#lunch.py
import datetime

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
  

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order', methods=('GET', 'POST'))
def order_lunch():
    form = forms.LunchOrderForm()
    if form.validate_on_submit():
        models.LunchOrder.create(
            user=g.user._get_current_object(),
            date=form.date.data,
            order=form.order.data.strip()
        )
    return render_template('lunch.html', form=form)


@app.route('/today')
@login_required
def today():
    order = models.LunchOrder.select().where(
        models.LunchOrder.date == datetime.date.today() &
        models.LunchOrder.user == g.user._get_current_object()
    ).get()
    return render_template('today.html', order=order)
  

@app.route('/cancel_order/<int:order_id>')
@login_required
def cancel_order(order_id):
    try:
        order = models.LunchOrder.select().where(
            id=order_id,
            user=g.user._get_current_object()
        ).get()
    except models.DoesNotExist:
        pass
    else:
        order.delete_instance()
    return redirect(url_for('index'))


@app.route('/follow/<int:user_id>')
@login_required
def follow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.create(
            from_user=g.user._get_current_object(),
            to_user=user
        )
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))
  

@app.route('/unfollow/<int:user_id>')
@login_required
def unfollow(user_id):
    try:
        user = models.User.get(
            models.User.id == user_id
        )
        models.Relationship.get(
            models.Relationship.from_user==g.user._get_current_object(),
            models.Relationship.to_user==user
        ).delete_instance()
    except (models.DoesNotExist, models.IntegrityError):
        pass
    return redirect(url_for('index'))


@app.route('/profile/<int:user_id>')
def profile(user_id):
    user = models.User.select().where(
        models.User.id == user_id
    ).get()
    return render_template('profile.html', user=user)
        
    
 #model.py

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase(':memory:')


class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')
    
    class Meta:
        database = DATABASE
        
    @property
    def following(self):
        return (
            User
            .select()
            .join(Relationship, on=Relationship.to_user)
            .where(Relationship.from_user == self)
        )

    @property
    def followers(self):
        return (
            User
            .select()
            .join(Relationship, on=Relationship.from_user)
            .where(Relationship.to_user == self)
        )

    
    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )


class LunchOrder(Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(User, related_name="orders")


class Relationship(Model):
    from_user = ForeignKeyField(User, related_name="relationships")
    to_user = ForeignKeyField(User, related_name="related_to")
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        indexes = (
            (('from_user', 'to_user'), True),
        )


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, LunchOrder], safe=True)
    DATABASE.close()
