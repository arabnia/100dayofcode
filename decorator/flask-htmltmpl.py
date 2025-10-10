from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email_var = request.form['email']
        password_var = request.form['password']
        return redirect(url_for("user", email=email_var, password=password_var))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    email_varr = request.args.get('email')
    password_varr = request.args.get('password')
    return render_template("userlogin.html",email=email_varr, password=password_varr)

app.run(port=8080,debug=True)