# imports
from flask import Flask
'''
    1. create an instance of the Flask
    2. WSGI(Web Server Gateway Interface) application
'''
# step-1: initialize the app
app = Flask(__name__)

# step-2: Create a basic route
@app.route("/")  # @ is a decorator for define the route
def welcome():
    return "Welcome to this world of flask"

@app.route("/hello")
def hello_world():
    return "hello world"

@app.route("/home")
def home_page():
    return "hello this is home page bla bla bla 1234"


# start or entry point of this project
if __name__ == "__main__":
    app.run(debug=True)  # debug for alawys update without restart