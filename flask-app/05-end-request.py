g - A global object that Flask uses for passing information between views and modules.
before_request - A decorator to mark a function as running before the request hits a view.
after_request - A decorator to mark a function as running before the response is returned.

#Import the g object from the flask library.
#add a function named before_request that sets g.db to the DATABASE variable in models and calls the .connect() method.
#The function should be decorated with the before_request decorator.

#create a function named after_request that takes a response object. 
#The function should close the g.db connection and return the response. 
#You should decorate the function with after_request.

from flask import Flask, g

import models

app = Flask(__name__)

@app.before_request
def before_request():
    '''connect to the database before each request'''
    g.db = models.DATABASE
    g.db.connect()
    
@app.after_request
def after_request(response):
    '''connect to the database before each request'''
    g.db.close()
    return response
