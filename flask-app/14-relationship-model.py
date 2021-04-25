indexes - A list of indexes to create on the model. These could be fields to index for faster searches or, as in our case, fields to make unique. More information
.join() - A query that references another table or another query.


    def following(self):
        """The users that we are following."""
        return (
            User.select().join(
                Relationship, on=Relationship.to_user
            ).where(
                Relationship.from_user == self
            )
        )
    
    def followers(self):
        """Get users following the current user"""
        return (
            User.select().join(
                Relationship, on=Relationship.from_user
            ).where(
                Relationship.to_user == self
            )
        )
      

      
class Relationship(Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')
    
    class Meta:
        database = DATABASE
        indexes = (
            (('from_user', 'to_user'), True)
        )
      
      
#Add a new model named Relationship. It should have a ForeignKeyField, related to User. 
#The field should be named from_user with a related_name of "relationships".
#Now add a second ForeignKeyField to Relationship. 
#This one, named to_user, should also point to User and have a related_name of "related_to".
#Now, add a third field, created_at, that's a DateTimeField with a default of datetime.datetime.now.
#Finally, add the class Meta to the Relationship model. The database should point to DATABASE. 
#You also need to add indexes to the model to make it unique. 
#The index should be a tuple with a tuple of the two foreign key fields and True. 
#Make sure you have a comma at the end like this - (( , ), ),
class Relationship(Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = DATABASE
        indexes = (
            (('from_user', 'to_user'), True),
        )


