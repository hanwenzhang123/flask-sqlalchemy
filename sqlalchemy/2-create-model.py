#echo = True adds info to console when it runs
#echo = False - clear up the console, it will remove additional messages when running the file
# session iw always watching

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo = False)    #create a local user.db
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()   #base here itself is a class so we capitalize

class User(Base):
  __tablename__ = 'users'
                            #here we create table
  id = Column(Integer, primary_key = True)
  name = Column(String)
  fullname = Column(String)
  nickname = Column(String)
  
  def __repr__(self):         #return the full user information
    return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'
              #Key-value pairs are the key to creating an entry.
  
  if__name__ = '__main__':
    Base.metadata.create_all(engine)    #connect engine with model classs to create database table
#     meg_user = User(name='Hanwen', fullname='Hanwen Zhang', nickname='Helen')
#     print(meg_user.name)  
#     print(meg_user.id)  #none
#     session.add(meg_user)     #add() adds one entry to the database
#     session.commit()    #this commit add our list to the database
#     print(session.id)
                #   add_all() adds multiple entries to a database
    session.add_all([User(name='Grace', fullname='Grace Hopper', nickname='Pioneer'), 
                User(name='Alan', fullname='Alan Turing', nickname='Computer Scientist'),  
                User(name='Katherine', fullname='Katherine Johnson', nickname='') ]   #this can be a variable instead
    session.commit()    #need commit to commit to the session, otherwise nothing saved
                
    for user in new_users:
         print(user.id)
                
# in the shell
sqlite 3 users.db
.table    #users
SELECT * FROM users;  #all the users will show up
                
#in the console - update/change entry
>>> import models
>>> jethro = models.User(name='Jethr', fullname='Jethro Amendola', nickname= 'Bubba';)
>>> models.session.add(jethro)
>>> models.session.new  #only track new entry
>>> jethro.name = 'Jethro' # we make change to the name
>>> models.session.commit()   #save the entry change, commit to the database
>>> models.session.dirty    #track past entry

#in the console - filter entry
>>> import models
>>> jethro = models.session.query(models.User).filter(models.User.name == 'Jethro').one() #only one entry
>>> jethro
>>> jethro.name = 'Bubba' 
                         
# rollback - like an undo buttton when we don't want the change to happen, everything will be removed
>>> jethro = models.User(name='Aang', fullname='Avatar Aang', nickname= 'Aangie';)
>>> models.session.add(aang)
>>> models.session.rollback()   #nothing will be store in both dirty and new

# detele - delete a committed entry
>>> models.session.commit()
>>> models.session.delete(aang)   #if we try to run query, no one aang
>>> models.session.commit()
                
                
                
#exercise 
                
1 - create database model
# First, import create_engine and declarative_base correctly from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#Create a variable called engine and set it equal to create_engine. 
#Use create_engine to create a SQLite database called movies.db and set echo to False. 
#Next, create a variable named Base and set it equal to declarative_base. Then create the model class. 
#It should be called Movie, and it takes Base as an argument (it inherits from Base). 
#Inside of the class, set the __tablename__ to ’movies’.
engine = create_engine('sqlite:///movies.db', echo = False) 
Base = declarative_base()

class Movie(Base):
    __tablename__ = ’movies’
                
# Finally, your table needs some columns. 
# Add Column, Integer, and String to your sqlalchemy imports. 
# Create an id column that holds numbers and is a primary key. 
# Create two more columns called movie_title and genre. Both columns hold strings.

    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    genre = Column(String)

                
                
# Now that your movie database model has been created, it’s time to add an entry. 
# First, import sessionmaker from sqlalchemy.orm. 
# After the engine variable, create a new variable called Session that uses sessionmaker to bind the engine. 
# Then create a variable called session that calls Session.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(‘sqlite:///movies.db’, echo=False)
Base = declarative_base()

class Movie(Base):
    __tablename__ = ‘movies’

    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    genre = Column(String)

#Use a variable named new_movie. Create a Movie() with whatever movie_title and genre you want. Then add your movie to session.
  if__name__ = '__main__':
    Base.metadata.create_all(engine)
    new_movie = Movie(movie_title='A', genre='B')
    session.add(new_movie)
    #To add your movie to the database, you need to commit it. 
    session.commit()
    #The movie theater is no longer showing your movie. Delete it from the database.
    session.delete(new_movie)
                
