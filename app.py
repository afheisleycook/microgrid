import random
import secrets
from sqlite3 import Connection, Cursor

from flask import(Flask, redirect, render_template, session, request, request_finished, flash,copy_current_request_context)
import sqlite3
import  datetime
import  logging

"""
data = {
    "home" : {
        "title":"home are",
        "peak time":datetime.datetime.now(),
        "add time":"added now",
    },
        "la": {
            "title": "la area",
            "peak time": datetime.datetime.now(),
            "add time": "added now",

        }
}
"""
app = Flask(__name__)
app.secret_key = secrets.token_hex()
loggedin = False
import sqlite3
@app.route("/blog/manage")
def dash():
    try:
        if loggedin:
            return render_template("/dash/index.html")
        if not loggedin:
            return redirect("/")
    except Exception as e:
        error = e.args
        return render_template("error/index.html",error=error)

@app.route("/")
def Home():
    """:return main page"""
    return redirect("/blog")
@app.route("/blog")
def main():
    """
    :return main page
    :return:
    """
    db = sqlite3.connect("app.db")
    conn = db.cursor()
    posts = conn.execute("select * from energy").fetchall()
    return render_template("index.html",posts=posts)
@app.route("/blog/auth")
def auth():
    return render_template("login.html")
@app.route("/blog/auth/login",methods=["post"])
def login():
    db: Connection = sqlite3.connect("app.db")
    connect: Cursor = db.cursor()
    username = request.form["username"]
    useremail = request.form["useremail"]
    userpassword = request.form["userpassword"]
    Auth = db.execute(f"select * from MUSER Where MUSER_USERNAME='{username}' or MUSER_USEREMAIL='{useremail}' and MUSER_PASSWORD='{userpassword}'")
    Auth_data = Auth.fetchall()
    if Auth_data == Auth:
        loggedin=True
        redirect("/blog/manage")
    else:
        loggedin = False
        return redirect("/blog/auth")



app.run(port=8080,debug=True)