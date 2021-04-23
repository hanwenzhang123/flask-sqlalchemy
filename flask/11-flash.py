flash(): This function stores a message in the session that will self-destruct after the response is returned.

get_flashed_messages(): This function gets all of the flash messages stored in the session.

app.secret_key: This configuration attribute stores the secret key that all messages are cryptographically signed with.

{% with %}: The Flask template version of Python's with block. Let's you temporarily define a variable. Must be closed with {% endwith %}.
  
  
  
  #Import flash from Flask.
#Add a secret_key attribute to the app object.
#flash() a message in the fishy() view before the return. The message can have any content you want.
from flask import Flask, redirect, url_for, render_template, flash

app = Flask(__name__)
app.secret_key = 'dsfjhkshfjkhdfjaskhkaajkf' #better when it is random


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fishy')
def fishy():
    flash("Hello")
    return redirect(url_for('index'))
  
  
  
  #Question
  How would I show the message "Thanks for answering!" to visitors as a temporary message?
  flash("thank you for visiting")

  
 
