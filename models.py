from sqlalchemy.ext.hybrid import hybrid_property
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    email = db.Column(db.String(100))
    password_hash = db.Column(db.String(128))
    
    @property
    def password(self):
        raise AttributeError('password not readable')
    
    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)
