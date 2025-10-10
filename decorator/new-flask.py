from flask import Flask, redirect, jsonify, url_for
app = Flask('my_app')
@app.route("/")
def index():
    return("<h2> this is the index page</h2>")

@app.route("/static")
def moamel():
    return(f"<h1> static page</h1>")

@app.route("/<user>")
def user_name(user):
    return(f"<h2> this is the index page for {user}</h2>")

@app.route("/admin")
def admin():
    return redirect("static")

app.run('0.0.0.0',port=8080)