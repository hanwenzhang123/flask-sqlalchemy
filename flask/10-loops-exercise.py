#exercise 1
#Your template has been given a list named options. 
#Loop through each item in options and create an <li> inside the <ul>. Print out the name key of each item.

from flask import Flask, render_template

from options import OPTIONS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('options.html', options=OPTIONS)
  
#HTML
<ul>
  {% for item in options %}
  <li>{{ item['name'] }}</li>
  {% endfor %}
</ul>




#exercise 2
#Loop through each of the teachers in teachers and create an <li> for them in the provided <ul>. 
#Inside the <li>, create an <h2> that holds the teacher's 'name' key.

#Now add a new <ul> inside of the <li> with a class of "courses". 
#Inside this <ul> loop through the teacher's 'courses' key, creating an <li> for each course and printing the course.

from flask import Flask, render_template

from teachers import TEACHERS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("teachers.html", teachers=TEACHERS)
  
#HTML
  <ul class="teachers">
  {% for teacher in teachers %}
  <li>
    <h2>{{ teacher['name'] }}</h2>

    <ul class="courses">
      {% for course in teacher['courses'] %}
      <li>{{ course }}</li>
      {% endfor %}
    </ul>
  </li>
  {% endfor %}
</ul>



#question
I have a list named names. I want to loop over it and print out the names. Complete the following code:
{% for name in names %}
