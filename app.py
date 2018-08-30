from flask import Flask, render_template
from Model.Server import User, Instances


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/admin")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.debug = True
    app.run(ssl_context=('cert.pem', 'key.pem'))
