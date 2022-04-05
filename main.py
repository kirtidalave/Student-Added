import flask
from flask import Flask, render_template,request

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

@app.route("/register", methods = ["GET", "POST"])
def regis():
    if request.method=="POST":
        getName=request.form["name"]
        getAdmno = request.form["admno"]
        getRollno = request.form["Rollno"]
        getBranch = request.form["br"]
        getSemester= request.form["sem"]
        getDOB = request.form["dob"]
        getUsername = request.form["username"]
        getPass= request.form["pass"]
        print(getName)
        print(getAdmno)
        print(getBranch)
        print(getRollno)
        print(getSemester)
        print(getSemester)
        print(getDOB)
        print(getUsername)
        print(getPass)
    return render_template("register.html")



if __name__=="__main__":
    app.run()

