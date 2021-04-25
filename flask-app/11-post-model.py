ForeignKeyField - A field that points to another database record.



#Create a new Model class with the name LunchOrder. Give it a TextField attribute named order.
#Now add a DateField (not DateTimeField) to the LunchOrder model. Name it date and do not give it a default value.
#add a ForeignKeyField to your LunchOrder model. Name it user. user should be related to the User model and the related_name should be "orders".

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
    
    @classmethod
    def new(cls, email, password):
        cls.create(
            email=email,
            password=generate_password_hash(password)
        )

class LunchOrder(UserMixin, Model):
    order = TextField()
    date = DateField()
    user = ForeignKeyField(
        rel_model=User,
        related_name="orders"
    )

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()
    
    
     
