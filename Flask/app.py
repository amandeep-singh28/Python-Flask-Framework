from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = 'supersecret' # Whenever you will use session, you have to use this

#homepage login page
@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username # store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials. Try again", mimetype = "text/plain") # It tells browser what content you will send back
    
    return '''
            <h2> Login Page </h2>
            <form method = "POST">
                Username: <input type = "text" name = "username"> <br>
                Password: <input type = "text" name = "password"> <br>
                <input type = "submit" value = "Login">
            </form>
'''

# Welcome page(after login)

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2> Welcome, {session["user"]}! </h2>
        <a href = {url_for('logout')}> Logout </a>
    '''
    return redirect(url_for("login"))

#Logout route
@app.route("/logout")
def logout():
    session.pop("user", None) #session["user"] = "amandeep"
    return redirect(url_for("login"))
    