from flask import Flask
from dotenv import load_dotenv
import os
from flask_restx import Api
from app.routes import home, user
from app.database import db, migrate


# load environment variables from .env file
load_dotenv()


app = Flask(__name__)

app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("TIDB_DATABASE_URL")

# bind the db to the app
db.init_app(app)
migrate.init_app(app, db)

api = Api(
    app, 
    version='1.0.0', 
    title='Resume Tailor Agent API',
    description='An API for tailoring resumes to job descriptions using AI agents.',
    doc='/docs',  # Swagger UI will be available at /docs
    default_mediatype='application/json',
)

# add the routes to the API
api.add_namespace(home, path="/api/home")
api.add_namespace(user, path="/api/user")
api.add_namespace(user, path="/api/users")



if __name__ == "__main__":
    app.run(debug=True)

