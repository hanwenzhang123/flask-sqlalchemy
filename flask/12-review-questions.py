Peewee's import convention isn't one we normally use. Which answer below is Peewee's convention?
from peewee import *

What Flask method shows a temporary message to the user?
flash()

What is the "magic" directory where Flask looks for HTML files to compile and render?
templates/

Finish this bit of code to make Flask compile an HTML template named "archive.html".
return render_template("archive.html")

Which Peewee field type would I use to store large blocks of text?
TextField()

In the following query, I want to change the sorting of my records. How would I sort them based on their published attribute so I get the oldest first?
Entry.select().order_by('published')
