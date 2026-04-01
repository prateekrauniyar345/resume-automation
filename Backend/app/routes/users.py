from flask_restx import Resource, Namespace
from datetime import datetime

user = Namespace(
    "user",
    description="User management endpoints", 
    ordered=True,
)

@user.route("/")
class Users(Resource):
    def get(self):
        return {"message": "Get all users"}
    
    def post(self):
        return {"message": "Create a new user"}

