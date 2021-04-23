The JSON library docs. 99% of the time, you won't need anything more than .loads() and .dumps().

Response: A response is the data that the server, Flask, sends back to the client.
make_response(): This function generates the entire response object that'll be sent back to the client, but lets you store it in a variable for further manipulation.
response.set_cookie(): Sets a cookie on the response object. Takes name for the cookie and a value.
json.dumps(): This method turns a Python data structure (list, string, dictionary, etc) into a JSON string.
json.loads(): This method turns a JSON string into a Python object.

  
#questions
When we create a cookie, we have to attach it to the response. What function gives us access to the response?
make_response()
from flask import make_response

How would you get all of the key & value pairs from the form?
request.form.items()

Set a cookie named "name" to "Treehouse"
resp = make_response()
resp.set_cookie("name", "Treehouse")

What json method creates a string?
dumps()


#exercise
#Add an import for the make_response function from Flask.
#add a variable named response and set it's value to make_response().
#set a cookie on the response object using the response.set_cookie method. 
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/save')
def save():
    response = make_response()
    response.set_cookie('treehouse', 'python')
    return response

  
  
  
  #question
  I need a response object before I can attach a cookie. Help me out:

response = make_response()
response.set_cookie('thanks', 'a bunch!')
