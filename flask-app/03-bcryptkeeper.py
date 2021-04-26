pip install flask-bcrypt

#In the console
python
>>>from flask_bcrypt import generate_password_hash
>>>generate_password_hash('secret')
>>>generate_password_hash('secret', 10)

>>> from flask_bcrypt import generate_password_hash
>>> generate_password_hash('secret')
b'$2b$12$mxLiHo9YcGAjX1XkAMnjW.SerTRX3qVi/j6vk6VNcmpof8pRtl0V.'
>>> hashed_pw = generate_password_hash('secret')
>>> hashed_pw 
b'$2b$12$X1IQHPXbXxzS9QloY24cl.SkwgswUuuq3bBO.px1yOIbPWZ7aL6a.'
>>> hashed_pw == generate_password_hash('secret')
False
>>> from flask_bcrypt import check_password_hash
>>> check_password_hash(hashed_pw, 'secret')
True


Notes
flask.ext.bcrypt - The path where Flask Bcrypt is available.
generate_password_hash() - function to generate a hash from a string. Takes an optional number of rounds of hashing to use. More rounds always makes the process take longer.
check_password_hash() - function to check a hash against a string to see if they match.



#exercise
#Import both generate_password_hash and check_password_hash from Flask-Bcrypt.
#Now create a function named set_password that takes a user and a password that is a string. 
#Hash the password, set the user.password attribute to the hashed password, and return the user.

from flask.ext.bcrypt import check_password_hash, generate_password_hash

def set_password(user, password):
    user.password = generate_password_hash(password)
    return user

def validate_password(user, password):
    return check_password_hash(user.password, password)
  
  
   
