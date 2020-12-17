

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

if  __name__ == '__main__':
     app.run(port=9000,debug=True)