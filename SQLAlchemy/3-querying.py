#console

source ./env/bin/activate
python3   #into the terminal shell now

import models
models.session.query(models.Users)  #here we get a query object back, we need to print it out by using for loop
for user in models.session.query(model.User):
  print(user) #here all our our users are printed out like User(name=Megan, fullname=Megan Amendola, nickname=Meg)

for user in models.session.query(models.User.name):
  print(user) #here we return back as a tuple like ('Megan', )

for user in models.session.query(models.User.name):
  print(user.name)  #here we print out name directly like Megan

for user in models.session.query(models.User.name).order_by(models.User.name):
  pirnt(user.name) # here all names print out in alphabetic order
  
for user in models.session.query(models.User.name).order_by(models.User.name.desc()): 
  pirnt(user.name) # here all names print out in descending order
  
for user in models.session.query(models.User.name).order_by(models.User.name)[:2]: 
  pirnt(user.name) #only the first two usernames will be printed out
  
for user in models.session.query(models.User.name).order_by(models.User.name)[2:4]: 
  pirnt(user.name) #start from 2 and stop at 4
  
models.session.query(models.User).all()    #return all the list -  all() returns a list of matching entries instead of a tuple.
models.session.query(models.User).order_by(models.User.name).first()    #return the first user in he list aphabetically
models.session.query(models.User).filter_by(name='Jethro')  #take keyword document
models.session.query(models.User).filter_by(models.User.name=='Jethro') #instead of key value pair, here we only focus on jethro

for user in models.session.query(models.User).filter(models.User.name=='Jethro'):
  print(user)   #here we print out the user information
  

#exercise

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine(‘sqlite:///movies.db’, echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Movie(Base):
    __tablename__ = ‘movies’

    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    genre = Column(String)


# Create a variable called romance_movies. It should hold all of the movies with a genre of 'Romance'.
romance_movies = session.query(Movie).filter_by(genre=='Romance')

#Create a variable named all_movies. It should hold all of the movies in the database in alphabetical order.
all_movies = session.query(Movie).order_by(Movie.movie_title)

# Create a new variable called the_movies that holds a query to find all products with ‘%The%’ in the movie_title and counts the number of returned values. 
# *Hint:* Use filter() with .like()
the_movies = session.query(Movie).filter(Movie.movie_title.like('%The%')).count()



# Questions
What would you add to this query to return a list instead of a tuple? 
session.query(Sales).all()

Which of the following will sort items in the database by year in descending order?
session.query(Sales).order_by(Sales.year.desc())

You updated an entry to fix a spelling error. What would you call to check that session has picked up this change?
session.dirty

Chaining function calls is allowed in SQLAlchemy
session.query(Sales).filter(Sales.year==2015).filter(Sales.price > 5)
  

                                                       
