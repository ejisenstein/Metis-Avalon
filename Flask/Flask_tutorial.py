from flask import Flask, redirect, url_for, render_template, request, session, flash

#from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     # if request.method =="POST":
#     #     session.permanent = True
#     #     user =
#     pass

if __name__ == "__main__":
    app.run(debug=True)
