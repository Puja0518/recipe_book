from flask_restful import Resource, Api, request
import uuid
import random
from random import *
import datetime
from models import db, Users, Post, Comments, Like, Follow, Favourite, Food
from sqlalchemy import or_
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
                    contact=data["contact"],
                    address=data["address"],
                    created_date=datetime.datetime.now()
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
class ForgotPass(Resource):
    def post(self):
        data = request.get_json()
        print("password====", data)

        rec = db.session.query(Users).filter(Users.email == data["email"]).first()
        if rec:
            rec.password = data["new_password"]
            db.session.commit()
            return { "message": "Password updated succesfully!!"}
        else:
            return { "message": "User doesnot exist"}

class UpdateUser(Resource):
    def post(self):
        data = request.get_json()
        print("updated data", data)

        rec = db.session.query(Users).filter(Users.email == data["email"]).first()
        if rec:
            rec.contact_number = data["contact"]
            rec.address = data["address"]
            db.session.commit()
            return { "message": "Profile has been updated successfully!!!"}
        else:
            return{ "message": "User does not exist"}

def GenerateId():
    id_ = randint(10000,10000000)
    print("id  --- " , id_)
    return id_

class Recipe_Post(Resource):
    def post(self):
        data = request.get_json()
        print("post data", data)
        data["post_id"] = GenerateId()
        post_rec = db.session.query(Post).filter(Post.post_id == data["post_id"]).first()
        if post_rec:
            data["post_id"] = GenerateId()
        
        rec = Post( post_id = data["post_id"],
                    user_id = data["user_id"],
                    description = data["description"],
                    ingrident = data["ingrident"],
                    procedure = data["procedure"],
                    file_name = data["file_name"],
                    created_date=datetime.datetime.now())
        db.session.add(rec)
        db.session.commit()
        #--------
        return { "message": "User Successfully Posted!!",
                "code": 200}

        
class GetId(Resource):
    def get(self):
        idx = GenerateId()
        return idx


class Comment(Resource):
    def post(self):
        data = request.get_json()
        print("comment data", data)
        data["comment_id"] = GenerateId()
        comment_rec = db.session.query(Comments).filter(Comments.comment_id == data["comment_id"]).first()
        if comment_rec:
            data["comment_id"] = GenerateId()
        
        rec = Comments( comment_id = data["comment_id"],
                        user_id = data["user_id"],
                        post_id = data["post_id"],
                        comment = data["comment"],
                        created_date=datetime.datetime.now())
        db.session.add(rec)
        db.session.commit()
        #--------
        return { "message": "User has been commented!!",
                "code": 200}

        
class GetCommentId(Resource):
    def get(self):
        idx = GenerateId()
        return idx

class LikeIt(Resource):
    def post(self):
        data = request.get_json()
        print("like data", data)
     
        rec = Like( object_id = data["object_id"],
                    user_id = data["user_id"],
                    like_date=datetime.datetime.now())
        db.session.add(rec)
        db.session.commit()
        #--------
        return { "message": "Liked the post/comment {}".format(data["object_id"]),
                 "code": 200}

class GetLike(Resource):
    def get(self):
        data = dict(request.args)
        count = db.session.query(Like).filter(Like.object_id == data["object_id"]).count()
        return {"message": "{} has {} likes".format(data["object_id"],count)}

class Subscribe(Resource):
    def post(self):
        data = request.get_json()
        print("follow data",data)

        rec = Follow(following = data["following"],
                     follower = data["follower"],
                     follow_date = datetime.datetime.now())
        db.session.add(rec)
        db.session.commit()

        return { "message": "{} is now following to {}".format(data["following"],data["follower"])}

class Favourite(Resource):
    def post(self):
        data = request.get_json()
        print("data:",data) 

        rec = Favourite(user_id = data["user_id"],
                        post_id = data["post_id"],
                        created_date = datetime.datetime.now())
        db.session.add(rec)
        db.session.commit()

        return { "message": "{} is your favourite post".format(data["post_id"]),
                "code": 200}

class Search(Resource):
    def post(self):
        data = request.get_json()
        search_word = data["search"]
        orm_query = db.session.query(Food)
        if "search" in data.keys():
            #print("----------- i am here !!!!!-----------")
            key = "search"
            search_query = data.get(key)
            cols_to_search = [
                "country",
                "state",
                "zone",
                "dishes"
            ]
            filter_list = []
            for filter_key in cols_to_search:
                search_attribute = getattr(Food,filter_key)
                filter_list.append(search_attribute.ilike("%" + search_query))

            orm_query = orm_query.filter(or_(*filter_list))
        db_obj = Database()
        # tmp = []
        # for row in orm_query:
        #     rec = db_obj.row2dict(row)
        #     tmp.append(rec)
        # return tmp
        return ([db_obj.row2dict(row) for row in orm_query])


class DishesType(Resource):
    def get(self):
        dishes = db.session.query(Food.dishes).all()
        result = []
        for dt in dishes:
            result.append(dt[0]) 
        return {"message": "List of Dishes",
                "data": result}
class StateList(Resource):
    def get(self):
        states = db.session.query(Food.state).all()
        result = []
        for st in states:
            result.append(st[0])
        return {"message": "List of states",
                "data":list(set(result))}

class ZoneList(Resource):
    def get(self):
        zones = db.session.query(Food.zone).all()
        result = []
        for zn in zones:
            result.append(zn[0])
        return {"message": "List of zone",
                "data":list(set(result))}




