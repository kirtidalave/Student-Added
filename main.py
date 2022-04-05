
from flask import Flask, render_template,request
import sqlite3
conn=sqlite3.connect("StudentManagementSystem.db")

listOfTables=conn.execute("SELECT name from sqlite_master WHERE type='table' AND name='STUDENT' ").fetchall()

if listOfTables!=[]:
    print("Table Already Exists ! ")
else:
    conn.execute(''' CREATE TABLE STUDENT(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT,COLLEGE_NAME TEXT, BRANCH TEXT,
    ADMNO INTEGER, PASSWORD TEXT, DOB TEXT
   ); ''')
print("Table has created")

app = Flask(__name__)

@app.route("/")
def StudentData():
    return render_template("login.html")


@app.route("/register", methods = ["GET", "POST"])
def regis():
    if request.method=="POST":
        getName=request.form["name"]
        getClgName = request.form["college_name"]
        getBranch = request.form["br"]
        getAdmno= request.form["admno"]
        getDOB = request.form["dob"]
        getPass= request.form["pass"]
        getcnfPass= request.form["cnf_pass"]
        print(getName)
        print(getClgName)
        print(getBranch)
        print(getAdmno)
        print(getDOB)
        print(getPass)
        print(getcnfPass)
        try:
            conn.execute("INSERT INTO STUDENT(name,COLLEGE_NAME TEXT,BRANCH,ADMNO,PASSWORD,DOB) VALUES('"+getName+"','"+getClgName+"','"+getBranch+"','"+getAdmno+"','"+getPass+"','"+getDOB+"',)")
        except Exception as e:
            print(e)

    return render_template("register.html")

@app.route("/search")
def searchStudent():
    return render_template("search.html")

@app.route("/delete")
def deleteStudent():
    return render_template("delete.html")


if __name__=="__main__":
    app.run()

