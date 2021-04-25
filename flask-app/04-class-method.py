`@classmethod` that allows us to create an instance of the class from inside of it. 

class Email:
    to = None
    from = None
    subject = None
    content = None
If I want to make a new Email using the class constructor, that's easy. email = Email() and then fill in the attributes. Assuming there's a __init__() that handles setting the attributes, I can probably do that in one step.

But what if I want a method for immediately creating and sending the email? I either have to create an instance and then call .send() on the instance or I need a @classmethod way of generating one.

class Email:
    to = None
    from = None
    subject = None
    content = None

    @classmethod
    def create_and_send(cls, to, from, subject, content):
        cls(to=to, from=from, subject=subject, content=content).send()
This won't be a benefit to every class you create, but it's often a better way of approaching use cases where you don't need the class to hang around longer than needed to perform some action.



#exercise

#Add a @classmethod to User named new. 
#It should take two arguments, email and password. 
#Remember, @classmethods take cls as the first argument.
#cls.create() call, using the provided email and a hash of the passwor

import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

database = SqliteDatabase(':memory:')

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = CharField(default='')
    
    class Meta:
        database = database
        
    @classmethod
    def new(cls, email, password):
        cls.create(
        email=email,
        password=generate_password_hash(password)
        )
