'''
Import the PasswordHasher class from argon2 and then make a new variable, HASHER that's an instantiation of that class.
add a staticmethod to User that returns a hashed password. Name it hash_password and have it take a single argument, the password to hash.
Hash the password using HASHER's 'hash' method and return it.
update the create_user method so that it sets the User instance's password using the User.hash_password method you just created. 
'''
from argon2 import PasswordHasher

import datetime

from peewee import *

DATABASE = SqliteDatabase('recipes.db')
HASHER = PasswordHasher()


class User(Model):
    username = CharField(unique=True)
    password = CharField()
    
    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, username, password):
        try:
            cls.get(cls.username**username)
        except cls.DoesNotExist:
            user = cls(username=username)
            # TODO: hash user password here?
            user.password = user.hash_password(password)
            user.save()
            return user
        else:
            raise Exception("User already exists")  
            
    @staticmethod
    def hash_password(password):
        return HASHER.hash(password)
    
    def verify_password(self, password):
        return HASHER.verify(self.password, password)
    

class Recipe(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Recipe, Ingredient], safe=True)
    DATABASE.close()
