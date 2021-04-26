#the resources still need their fields defined and to use marshal or marshal_with.
#For this step, just create the ingredient_fields dictionary with a key for each field.
#now all of the methods need to be marshaled.
#Use marshal or marshal_with along with the ingredient_fields to make each method return a valid response.
#Make sure IngredientList.get returns a dictionary with a key named ingredients that holds all of the Ingredient instances.

from flask import Blueprint

from flask.ext.restful import (
    Resource, Api, reqparse, inputs,
    marshal, marshal_with, fields
)

import models

ingredient_fields = {
    'name': fields.String,
    'description': fields.String,
    'measurement_type': fields.String,
    'quantity': fields.Float,
    'recipe': fields.String
}


class IngredientList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'measurement_type',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'quantity',
            type=float,
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'recipe',
            type=inputs.positive,
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        ingredients = [marshal(ingredient, ingredient_fields)
                   for ingredient in models.Ingredient.select()]
        return {'ingredients': ingredients}

    @marshal_with(ingredient_fields)
    def post(self):
        args = self.reqparse.parse_args()
        ingredient = models.Ingredient.create(**args)
        return ingredient


class Ingredient(Resource):
    def __init__(self):
          self.reqparse = reqparse.RequestParser()
          self.reqparse.add_argument(
              'name',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'description',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'measurement_type',
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'quantity',
              type=float,
              required=True,
              location=['form', 'json']
          )
          self.reqparse.add_argument(
              'recipe',
              type=inputs.positive,
              required=True,
              location=['form', 'json']
          )
          super().__init__()

    @marshal_with(ingredient_fields)
    def get(self, id):
        ingredient = models.Ingredient.get(models.Ingredient.id==id)
        return ingredient

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(IngredientList, '/api/v1/ingredients')
api.add_resource(Ingredient, '/api/v1/ingredients/<int:id>')
