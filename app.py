from flask import Flask
from flask import render_template
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

app.run(host="0.0.0.0", debug=True)
