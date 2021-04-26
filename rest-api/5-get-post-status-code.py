#All of the methods are complete for the Recipe and RecipeList resources except for delete. It does the deletion but just sends back "Deleted!" which isn't very useful.
#Complete the method so that it sends back an empty response, the 204 status code, and a Location header with a URL for the RecipeList resource.

from flask import Blueprint, abort, url_for

from flask.ext.restful import Resource, Api, reqparse, inputs, marshal, marshal_with, fields

import models

recipe_fields = {
    'name': fields.String
}


def get_recipe_or_404(id):
    try:
        recipe = models.Recipe.get(models.Recipe.id==id)
    except models.Recipe.DoesNotExist:
        abort(404)
    else:
        return recipe


class RecipeList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    def get(self):
        return [marshal(recipe, recipe_fields) for recipe in models.Recipe.select()]
      
    @marshal_with(recipe_fields)
    def post(self):
        args = self.reqparse.parse_args()
        recipe = models.Recipe.create(**args)
        return (recipe, 201, {
            'Location': url_for('resources.recipes.recipe', id=recipe.id)
        })


class Recipe(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name',
            required=True,
            location=['form', 'json']
        )
        super().__init__()

    @marshal_with(recipe_fields)
    def get(self, id):
        return get_recipe_or_404(id)

    @marshal_with(recipe_fields)
    def put(self, id):
        recipe = get_recipe_or_404(id)
        args = self.reqparse.parse_args()
        query = models.Recipe.update(**args).where(models.Recipe.id==id)
        query.execute()
        return (get_recipe_or_404(id), 200, {
            'Location': url_for('resources.recipes.recipe', id=recipe.id)
        })

    def delete(self, id):
        query = models.Recipe.delete().where(models.Recipe.id==id)
        query.execute()
        return 'Deleted!', 204, {'Location': url_for('resources.recipes.recipes')}

recipes_api = Blueprint('resources.recipes', __name__)
api = Api(recipes_api)
api.add_resource(RecipeList, '/api/v1/recipes', endpoint='recipes')
api.add_resource(Recipe, '/api/v1/recipes/<int:id>', endpoint='recipe')
