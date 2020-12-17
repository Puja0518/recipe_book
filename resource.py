from flask_restful import Resource, Api, request
import uuid
from random import *
import datetime
from models import db, Users



class Database():

    def __init__(self):
        pass

    def row2dict(self,row):
        d = {}
        for column in row.__table__.columns:
            d[column.name] = str(getattr(row, column.name))
        return d


class Hello(Resource):
    def get(self):
        return "Hello! Welcome to Recipe Book!!"

# UserRegistration
class UserRegistration(Resource):
    # def get(self):
    #     return { "message": "User with get nethod allowed!!",
    #             "code": 200}

    def post(self):
        data = request.get_json()
        print("data sent ===>> ", data)
        #--- next add to database ---
        rec = Users(email= data["email"],
                    username=data["username"],
                    password=data["password"],
                    contact=data["contact"]
                    )
        db.session.add(rec)
        db.session.commit()
        #--------
        return { "message": "User has been registered!!",
                "code": 200}

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        print("login data====",data)

        rec=db.session.query(Users).filter(Users.email == data["email"]).first()
        if rec:
            pwd= rec.password
            if pwd==data["password"]:
                return { "message": "Login Successfully!!!",
                         "code": 200}

            else : 
                return { "message": "Incorrect password!!!"
                         "code: 400"}
        else :
            return { "message": "User not found"}
