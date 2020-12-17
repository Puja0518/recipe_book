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

    def __init__(self, email, username, password, contact):
        self.email = email
        self.username = username
        self.password = password
        self.contact_number = contact

    def __repr__(self):
        return '<id {}>'.format(self.id)
