#Use {{ and }} to print items in templates.
#Flask looks for templates in a directory named templates by default. 
#This directory should be in the same directory as your app script.
#templates directory: add.html & index.html

#simple_app.py
from flask import Flask
from flask import render_template   #import it for html

app = Flask(__name__)


@app.route('/') 
@app.route('/<name>')
def index(name='Treehouse'):
    return render_template("index.html", name=name)   # we have a seperate index.html file
                                 #in the index.html, we will use {{ name }} to put out the value

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template("add.html", **context) #need to make a seperate html file called add.html
#                          **context - unpack our context instead of using num1=num1, num2=num2 here
#in the app.html file, we will have the line {{num1}} + {{num2}} = {{num1+num2}}
app.run(debug=True, port=8000, host='0.0.0.0')


#exercise
#Add an import for render_template. It comes directly from the flask library.
#Use render_template() to render the "hello.html" template in hello().
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name="Treehouse"):
    return render_template("hello.html", name=name)

#Pass the name argument to the template. Print the name variable in the <h1> in the template.
<!doctype html>
<html>
<head><title>Hello!</title></head>
<body>
<h1>{{name}}</h1>
</body>
</html>
