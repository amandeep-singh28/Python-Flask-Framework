from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/submit", methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username == "aman123" and password == "pass":
    #     return render_template("welcome.html", name = username)
    valid_user = {
        'amandeep' : '123',
        'aman' : '123',
        'amandeep singh' : '123'
    }
    if username in valid_user and password == valid_user[username]:
        return render_template("welcome.html", name = username)
    else:
        return "Invalid credentials"