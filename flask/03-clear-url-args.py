from flask import Flask
#from flask import request  - we do not need to import request because the name from the route now

app = Flask(__name__)

@app.route('/') 
@app.route('/<name>')   #capture what comes after that '/',  here is the argument name
def index(name='Treehouse'): 
#  name = request.args.get('name', name)   # we do not need this line now because the name comes through the route
   return "Hello from {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')    #turn it into integer
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
  return '{} + {} = {}'.format(num1, num2, num1+num2)
           
app.run(debug=True, port=8000, host='0.0.0.0')


#exercise
#view args through url

#Add a new route to hello() that expects a name argument. 
#The view will need to accept a name argument, too.
#Update the response from hello() to say "Hello {name}", replacing {name} with the passed-in name.
#Now give hello() a default name argument of "Treehouse".
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name = "Treehouse"):
    return "Hello {}".format(name)
  
  
#Multiple views
#Add a view named multiply. Give multiply a route named /multiply. 
#Make multiply() return the product of 5 * 5. Remember, views have to return strings.
#default value 5* 5
#Mark both route arguments as ints.
#Add routes to allow floats or a combination of floats and ints.
#Change the response to multiply the two arguments and return their product.

from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:num1>/<int:num2>')
@app.route('/multiply/<float:num1>/<int:num2>')
@app.route('/multiply/<int:num1>/<float:num2>')
@app.route('/multiply/<float:num1>/<float:num2>')
def multiply(num1=5, num2=5):
    result = num1 * num2
    return str(result)
