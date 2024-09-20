from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from database import User

import datetime

app = Flask(__name__)

@app.route("/")
def top():
    return str(datetime.datetime.now())

@app.route("/kazu")
def kazu():
    return render_template("signup.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/create-user", methods=["POST"])
def create_user():
    nickname = request.form["nickname"]
    name = request.form["name"]
    password = request.form["password"]
    email = request.form["email"]
    print(nickname, name, password, email)
    User.create(
        nickname=nickname,
        name=name,
        password=password,
        email=email,
    )
    return redirect("/news")
app.run(host="0.0.0.0", debug=True)
