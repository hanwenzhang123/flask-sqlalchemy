


#app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
db = SQLAlchemy(app)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_type = db.Column(db.String())
    plant_status = db.Column(db.String())


#models.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
db = SQLAlchemy(app)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plant_type = db.Column(db.String())
    plant_status = db.Column(db.String())

#form.html
{% extends 'layout.html' %}

{% block content %}
    <form action="{{ url_form('form') }}" method="POST">
        <label for="type">Plant Type:</label>
        <input type="text" name="type" id="type" placeholder="Plant type">

        <p>Plant Status:</p>
        <label for="good">GOOD</label>
        <input type="radio" name="status" id="good">
        <label for="ok">OK</label>
        <input type="radio" name="status" id="ok">
        <label for="bad">BAD</label>
        <input type="radio" name="status" id="bad">
    </form>
{% endblock %}

#index.html
{% extends 'layout.html' %}

{% block content %}
    <h1>Our Plants:</h1>
  {% for plant in plants %}
    <div>
        <h2>{{ plant.plant_type}}</h2>
        <p>{{ plant.plant_status}}</p>
    </div>
  {% endfor %}
{% endblock %}
