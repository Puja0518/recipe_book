import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from random import *
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@127.0.0.1:5432/recipe_book"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# app.config["MONGOALCHEMY_DATABASE"] = "Backend_Python"
# app.config['MONGOALCHEMY_SERVER_AUtH'] = False
# db = MongoAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(),unique=True,nullable=False)
    username =db.Column(db.String(),unique=True,nullable=False)
    password = db.Column(db.String())
    contact_number = db.Column(db.String())
    address = db.Column(db.String())
    created_date = db.Column(db.DateTime())
    

    def __init__(self, email, username, password, contact, address, created_date):
        self.email = email
        self.username = username
        self.password = password
        self.contact_number = contact
        self.address = address
        self.created_date = created_date

    def __repr__(self):
        return '<id {}>'.format(self.id)
        #  migration

class Post(db.Model):
    __tablename__= "post"
    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer,unique=True,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    description = db.Column(db.String(),nullable=False)
    ingrident = db.Column(db.String(),nullable=False)
    procedure = db.Column(db.String(),nullable=False)
    file_name = db.Column(db.String())
    created_date = db.Column(db.DateTime())

    def __init__(self, post_id, user_id, description, ingrident, procedure, file_name, created_date):
        self.post_id = post_id
        self.user_id = user_id
        self.description = description
        self.ingrident = ingrident
        self.procedure = procedure
        self.file_name = file_name
        self.created_date = created_date

    def __repr__(self):
        return '<id {}>'.format(self.id)


class Comments(db.Model):
    __tablename__= "comments"
    id = db.Column(db.Integer,primary_key=True)
    comment_id = db.Column(db.Integer,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey("post.post_id"),nullable=False)
    comment = db.Column(db.String(),nullable=False)
    created_date = db.Column(db.DateTime())

    def __init__(self, comment_id, user_id, post_id, comment, created_date):
        self.comment_id = comment_id
        self.user_id = user_id
        self.post_id = post_id
        self.comment = comment
        self.created_date = created_date

    def __repr__(self):
        return '<id {}>'.format(self.id)
 
class Like(db.Model):
    __tablename__="likes"
    id = db.Column(db.Integer,primary_key=True)
    object_id = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    like_date = db.Column(db.DateTime())

    def __init__(self, object_id, user_id,like_date):
        self.object_id = object_id
        self.user_id = user_id
        self.like_date = like_date

    def __repr__(self):
        return '<id {}>'.format(self.id)

