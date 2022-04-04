import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def StudentDate():
    return render_template("student.html")

@app.route("/search")
def searchstudent():
    return render_template("search.html")
@app.route("/deleted")
def deletedstudent():
    return render_template("delete.html")

if __name__=="__main__":
    app.run()

