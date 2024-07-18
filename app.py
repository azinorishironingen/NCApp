from flask import Flask
import datetime

app = Flask(__name__)
@app.route("/")
def top():
    return str(datetime.datetime.now())
app.run(host="0.0.0.0")
