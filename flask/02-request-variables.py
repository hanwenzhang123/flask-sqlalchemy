global: A global is a variable that exists outside of the normal Python scopes. It is available everywhere.
query string: The part of a URL that comes after the ?. You'll notice that the information after this looks like keyword arguments.
request: request is a Flask global that represents the request that the client has made to your application. This contains things like cookies, the path, and, in our usage, the query string.


from flask import Flask
from flask import request #we need to import from Flask to have access to the query string

app = Flask(__name__)

@app.route('/') 
def index(name='Treehouse'):  #args. that hold argument in the request, like get and post key and value
  name = request.args.get('name', name) #if we get a name, use that name, otherwise use the default name
  return "Hello from {}".format(name)
    
app.run(debug=True, port=8000, host='0.0.0.0')


#exercise
#requesting args

#Import request from Flask. 
#Then update the index view to return "Hello {name}", replacing {name} with a name argument in the query string.
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name='hanwen'):
    name = request.args.get('name', name)
    return 'Hello {}!'.format(name)
