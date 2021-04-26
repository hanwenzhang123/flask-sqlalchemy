 #build an API for creating recipes. 
  
  #models.py
  
  import datetime

from peewee import *

DATABASE = SqliteDatabase('recipes.db')


class Recipe(Model):
    name = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


# TODO: Ingredient model
# name - string (e.g. "carrots")
# description - string (e.g. "chopped")
# quantity - decimal (e.g. ".25")
# measurement_type - string (e.g. "cups")
# recipe - foreign key

class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe)    # relationship to another model

    class Meta:
        database = DATABASE
        
        
        
#resource/ingredients.py
        
from flask.ext.restful import Resource

import models

class IngredientList(Resource):
    def get(self):
        return 'IngredientList'

class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'
