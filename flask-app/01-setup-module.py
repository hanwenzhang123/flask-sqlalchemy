#Import everything from the Peewee library. 
#Create a new model named User. Give User an email attribute that is a CharField(). email should be unique.

#Now add two more attributes/fields to User. The password field should be a CharField with a max_length of 100. 
#And the join_date field should be a DateTimeField with a default value of datetime.datetime.now.

#Finally, add a last field named bio that is a TextField. 
#It should have an empty string for its default value. This makes it optional.

import datetime
from peewee import *

class User(Model):
    email = CharField(unique=True)
    password = CharField(max_length=100)
    join_date = DateTimeField(default=datetime.datetime.now)
    bio = TextField(default="")
