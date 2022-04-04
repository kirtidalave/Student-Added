from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def StudentDate():
    return "Student Data"

@app.route("/search")
def searchstudent():
    return "required student is:"
@app.route("/deleted")
def deletedstudent():
    return "deleted student is:"

if __name__=="__main__":
    app.run()

