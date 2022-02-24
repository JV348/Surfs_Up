#Import the Flask dependency
from flask import Flask

# Create a new Flask instance called app
app = Flask(__name__)

## Create Flask Routes

# First flask route 
@app.route('/')
def hello_world():
    return 'Hello world'

## Run a Flask App

# Set the FLASK_APP environment variable to the name of our Flask file, app.py
export FLASK_APP=app.py