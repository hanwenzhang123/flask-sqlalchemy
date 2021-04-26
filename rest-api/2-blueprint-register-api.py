#make a Blueprint for each of the resources. Name the one in ingredients.py "ingredients_api" and the one in recipes.py "recipes_api"
#Create a new variable named api in each of the resources that's an Api instance for the Blueprint. 
#Then add both of the Resources to api. You can use whatever endpoint name you want, but make sure the URL pattern is like "/api/v1/[PLURAL RESOURCE]". 
#Remember to include the id argument in the appropriate URLs.
#You need to import the blueprints into app.py and register them both with app.

#api.py
from flask import Flask

from resources.ingredients import ingredients_api
from resources.recipes import recipes_api

app = Flask(__name__)
app.register_blueprint(ingredients_api)
app.register_blueprint(recipes_api)

if __name__ == '__main__':
    app.run()
    

#resources/ingredients.py
from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class IngredientList(Resource):
    def get(self):
        return 'IngredientList'


class Ingredient(Resource):
    def get(self, id):
        return 'Ingredient'
    
ingredients_api = Blueprint('resources.ingredients',__name__)
api = Api(ingredients_api)
api.add_resource(
    IngredientList,
    '/api/v1/ingredients',
    endpoint='ingredients'
)
api.add_resource(
    Ingredient,
    '/api/v1/ingredients/<int:id>',
    endpoint='ingredient'
)




#resources/recipes.py
from flask import Blueprint
from flask.ext.restful import Resource, Api

import models


class RecipeList(Resource):
    def get(self):
        return 'RecipeList'


class Recipe(Resource):
    def get(self, id):
        return 'Recipe'
    
recipes_api = Blueprint('resources.recipes',__name__)   
api = Api(recipes_api)
api.add_resource(
    RecipeList,
    '/api/v1/recipes',
    endpoint='recipes'
)
api.add_resource(
    Recipe,
    '/api/v1/recipes/<int:id>',
    endpoint='recipe'
)
