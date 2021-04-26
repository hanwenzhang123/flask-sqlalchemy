'''
The API needs to be able to validate input from users. 
Use reqparse and add arguments for each field in the Ingredient model to the IngredientList resource. 
Remember to add the RequestParser instance to the resource instance as self.reqparse.

name, description, and measurement_type should all be strings (the default)
quantity should be a normal Python float
recipe should be positive, which you'll get from inputs
They should all be required and have their location set to ["form", "json"].
'''

from flask import Blueprint

from flask.ext.restful import Resource, Api, reqparse, inputs

import models


class IngredientList(Resource):
    def get(self):
        return 'IngredientList'

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=["form","json"]
        )
        self.reqparse.add_argument(
            'description',
            required=True,
            location=["form","json"]
        )
        self.reqparse.add_argument(
            'measurement_type',
            required=True,
            location=["form","json"]
        )
        self.reqparse.add_argument(
            'quantity',
            required=True,
            location=["form","json"],
            type=float
        )
        self.reqparse.add_argument(
            'recipe',
            required=True,
            location=["form","json"],
            type=inputs.positive
        )


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'

ingredients_api = Blueprint('resources.ingredients', __name__)
api = Api(ingredients_api)
api.add_resource(IngredientList, '/api/v1/ingredients')
api.add_resource(Ingredient, '/api/v1/ingredients/<int:id>')

