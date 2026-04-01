from flask_restx import Resource, Namespace
from datetime import datetime

home = Namespace(
    "home", 
    description="Home endpoint for API status", 
)

@home.route("/")
class Home(Resource):
    def get(self):
        return {
            "message": "Welcome to RESUME TAILOR AGENT API",
            "status": "running",
            "code": 200,
            "date": datetime.now().isoformat()
        }