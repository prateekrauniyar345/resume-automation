from flask import Flask
from dotenv import load_dotenv
import os
from datetime import datetime
# load environment variables from .env file
load_dotenv()


app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message" : "Welcome to RESUME TAILOR AGENT API",
        "status" : "running", 
        "code" : 200, 
        "date" : datetime.now().isoformat()
    } 



if __name__ == "__main__":
    app.run(debug=True)

