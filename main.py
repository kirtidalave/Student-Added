import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hom():
    return render_template("slash.html")

@app.route("/search")
def sea():
    return render_template("search.html")

@app.route("/deleted")
def delete():
    return render_template("delete.html")

@app.route("/register")
def regis():
    return render_template("register.html")

if __name__=="__main__":
    app.run()

