View: A view is a function that returns an HTTP response. This response has to be a string but can be any string you want.
Route: A route is the URL path to a view. They always start with a forward slash / and can end with one if you want.

Local Setup Steps
Create a folder for your project
Open your folder in your IDE
Open the terminal in your IDE
Create a virtual environment: Mac: python3 -m venv env
Activate your environment: Mac: source ./env/bin/activate
Install Flask - pip install flask
Create requirements file - pip freeze > requirements.txt

#create an app:

#Import Flask from the flask library
from flask import Flask #in python we always name class with an upper case
#Create a new Flask instance as a variable named app. The name you pass to the Flask app should be __name__
app = Flask(__name__) # #use our current namespace is

#create a view:

#Add a view function named index. Give this view a route of "/". 
#Make the view return your name. You do not need to use app.run().
@app.route('/')  #route gives it a view after the '/'. #a function that wrap around another function, let you do things the function
def index():
    return 'Hanwen Zhang'
  
app.run(debug=True, port=8000, host='0.0.0.0')



#question
Attach the following view to my app with the route of /teachers.
@app.route('/teachers')
def teachers():
    return 'We have lots of teachers!'


What are the two magic directories for Flask to find template files and static files?
templates/ and static/


What global object represents a client asking for a view from your app?
request


How do you print something in a Flask template?
{{and}}
