from flask import Flask
from dotenv import load_dotenv
import os
from flask_restx import Api, Resource, Namespace
from datetime import datetime
# load environment variables from .env file
load_dotenv()


app = Flask(__name__)

app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'

@app.route("/", methods=["GET"])
def home():
    return {
        "message" : "Welcome to RESUME TAILOR AGENT API",
        "status" : "running", 
        "code" : 200, 
        "date" : datetime.now().isoformat()
    }

api = Api(
    app, 
    version='1.0.0', 
    title='Resume Tailor Agent API',
    description='An API for tailoring resumes to job descriptions using AI agents.',
    doc='/docs',  # Swagger UI will be available at /docs
    default_mediatype='application/json',
)


home = Namespace("home", description="Home endpoint for API status")

@home.route("/")
class Home(Resource):
    def get(self):
        return {
            "message" : "Welcome to RESUME TAILOR AGENT API",
            "status" : "running", 
            "code" : 200, 
            "date" : datetime.now().isoformat()
        } 


@home.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    
    def post(self, name):
        return {'hello': name}


api.add_namespace(home, path="/home")


if __name__ == "__main__":
    app.run(debug=True)

