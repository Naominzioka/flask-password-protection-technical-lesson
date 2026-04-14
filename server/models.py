from marshmallow import Schema, fields
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    #add a password hash
    _password_hash = db.Column(db.String)
    
    def __repr__(self):
        return f'User {self.username}, ID: {self.id}'
    
    
    @hybrid_property          #protect the password hash from being viewed by making it a hybrid property that raises an exception when accessed 
    def password_hash(self):
        raise Exception('Password hashes may not be viewed.')
    
    @password_hash.setter   #this is a setter method, so it will be called when we set the password_hash attribute of a User instance
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')
        
    def authenticate(self, password):   #verify that the password provided by the user matches the password hash stored in the database
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    

class UserSchema(Schema):
    id = fields.Int()
    username = fields.String()