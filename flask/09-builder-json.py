{% for x in y %}: You already know what for x in y: does in Python, but this is the template version. 
This will cause the enclosed code to be run as many times as there are things in y. Has to be followed by {% endfor %}.

{% if %}: The template version of Python's if condition. Closed with {% endif %}.


#exercise
#create a json string
#Import the json library.
import json

#Create a function named to_json that takes a single argument. 
#Convert the argument to string with the json library and return it.
def to_json(arg):
    return json.dumps(arg)
  
#Create a function named from_json that takes a single argument. 
#Parse the argument with the json library and return it.
def from_json(arg):
    return json.loads(arg)
