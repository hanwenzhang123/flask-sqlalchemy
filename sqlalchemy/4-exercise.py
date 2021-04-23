#app.py
from models import db, Plant, app
from flask import render_template, url_for, request, redirect


@app.route('/')
def index():
    plants = Plant.query.all()
    return render_template('index.html', plants=plants)


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.form:
        new_plant = Plant(plant_type=request.form['type'], 
                          plant_status=request.form['status'])
        db.add(new_plant)
        db.commit()
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/delete/<id>')
def delete(id):
    plant = Plant.query.get(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


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





#Question
Which of the following will pass an id variable in the URL from the HTML to your Python route?
{{url_for('index', id=plant.id)}}

Which of the following is the correct way to input a plant’s name variable into a template’s?
{{ plant.name }}

To loop through plant data passed into a template, you write _______ plant in plants _____ to start the loop and ____ to end the loop.
{% for plants in the plants %} {% endfor %}
