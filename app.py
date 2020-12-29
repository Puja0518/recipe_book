

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

#------- JWT -------
from flask_jwt_extended import JWTManager
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
jwt = JWTManager(app)

import resource

api.add_resource(resource.Hello, '/home')
api.add_resource(resource.UserRegistration, '/signin')
api.add_resource(resource.UserLogin, '/login')
api.add_resource(resource.ForgotPass, "/forgot_password")
api.add_resource(resource.UpdateUser, "/profile_update")
api.add_resource(resource.GetId, "/generate")
api.add_resource(resource.Recipe_Post,"/post")
api.add_resource(resource.Comment,"/comment")
api.add_resource(resource.LikeIt,"/like")
api.add_resource(resource.GetLike, "/get_like")
api.add_resource(resource.Subscribe, "/follow")
api.add_resource(resource.Favourite,"/favourite")

if  __name__ == '__main__':
     app.run(port=9000,debug=True)