from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello user! This is my first flask app"

@app.route("/about")
def about():
    return "This is about us page"

@app.route("/contact")
def contact():
    return("This is a contact us page")

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You sent data!"
    else:
        return "You are just viewing the form."