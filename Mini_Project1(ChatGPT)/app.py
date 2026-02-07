from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "my_secret_key"


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        session["name"] = request.form["student_name"]
        session["marks"] = int(request.form["marks"])

        marks = session["marks"]

        if marks >= 90:
            session["result"] = "Topper"
        elif marks >= 40:
            session["result"] = "Pass"
        else:
            session["result"] = "Fail"

        return redirect(url_for("result"))
    
    else:
        return render_template("form.html")

@app.route("/result")
def result():
    return render_template(
        "result.html",
        name=session.get("name"),
        marks=session.get("marks"),
        result=session.get("result")
    )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/help")
def help():
    return "This is the help page"

if __name__ == "__main__":
    app.run(debug = True)