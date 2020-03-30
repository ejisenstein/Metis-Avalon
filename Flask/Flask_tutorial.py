from flask import Flask, redirect, url_for, render_template, request, session, flash
from forms import RegistrationForm, LoginForm

#from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '93548cc0fde27fd878cb9aab95033646'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)



# @app.route("/login", methods=["POST", "GET"])
# def login():
#     # if request.method =="POST":
#     #     session.permanent = True
#     #     user =
#     pass

if __name__ == "__main__":
    app.run(debug=True)
