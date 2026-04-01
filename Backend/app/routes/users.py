from flask import request
from flask_restx import Resource, Namespace, fields
from app.services.user import get_users

user = Namespace(
    "user",
    description="User management endpoints",
    ordered=True,
)

user_response_model = user.model("UserResponse", {
    "id": fields.Integer,
    "user_name": fields.String,
    "email": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
})

user_create_model = user.model("UserCreate", {
    "user_name": fields.String(required=True),
    "email": fields.String(required=True),
})


@user.route("/")
class Users(Resource):

    @user.doc(params={
        "id": "User ID",
        "user_name": "user_name",
        "email": "User email",
    })
    @user.marshal_list_with(user_response_model)
    def get(self):
        """Get users with optional filters"""

        user_id = request.args.get("id", type=int)
        user_name = request.args.get("user_name", type=str)
        email = request.args.get("email", type=str)

        users = get_users(
            id=user_id,
            user_name=user_name,
            email=email
        )

        return [u.model_dump() for u in users], 200

    @user.expect(user_create_model, validate=True)
    @user.marshal_with(user_response_model, code=201)
    def post(self):
        """Create a new user"""

        data = request.get_json()

        new_user = create_user(
            user_name=data["user_name"],
            email=data["email"]
        )

        if not new_user:
            user.abort(400, "user_name or email already exists")

        return new_user.model_dump(), 201