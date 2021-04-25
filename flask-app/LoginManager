from flask_login import LoginManager

LoginManager - An appliance to handle user authentication.
user_loader - A decorator to mark the function responsible for loading a user from whatever data source we use.


#Add a secret_key attribute to app with a random value.

#Import the LoginManager from Flask-Login.

#Now create a LoginManager instance named login_manager. 
#Then run the init_app method, passing app as the argument.

#create a function named load_user that takes a user's id attribute as an argument. 
#Inside the function, look up a models.User instance with the id and return it. 
#Return None if the User doesn't exist. Decorate the function with @login_manager.user_loader.

from flask import Flask, g
from flask_login import LoginManager

import models

app = Flask(__name__)
app.secret_key='aefaae'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None
