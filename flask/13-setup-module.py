import datetime
from peewee import *

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = TextField(default="")
