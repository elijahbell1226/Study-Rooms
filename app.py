# Bring in the Flask class from the flask package, 
# The flask package is a folder full of code for handling web requests.
# flask (package name) Flask (a class/tool for building a web app.)
from flask import Flask

#Create web app and save in variable called 'app'
app = Flask(__name__)

#message displayed on screen when user opens app

#@app.route(...) "When someone visits this address ("/"),
#run the function underneath"
@app.route("/")

def say_hello():
    return "Hello"

