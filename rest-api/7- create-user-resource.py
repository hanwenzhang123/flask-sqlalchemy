'''
Add two new requirements to the RequestParser for "password" and "confirm_password". 
Both should be required and in either "form" or "json" locations.
inside of UserList.post, check that the "password" and "confirm_password" args are equal to each other. 
If they're not, raise an Exception. If they are equivalent, go ahead and create the user and send it back.
'''

from flask import Blueprint

from flask.ext.restful import Resource, Api, reqparse, marshal_with, fields

import models

user_fields = {
    'username': fields.String
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'confirm_password',
            required=True,
            help='No password verification provided',
            location=['form', 'json']
        )
        super().__init__()
      @marshal_with(user_fields)
      
    def post(self):
        args = self.reqparse.parse_args()
        if args.get('password') == args.get('confirm_password'):
            user = models.User.create(**args)
            return marshal(user, user_fields), 201
        return make_response(json.dumps({'error': 'Password and confirm_password do not match'}), 400)  


users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(UserList, '/api/v1/users')
