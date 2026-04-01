from flask import Flask
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()


app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)

