from flask import render_template, url_for, flash, redirect
from flask_avalon import app
from flask_avalon.models import User, Vote
from flask_avalon.forms import RegistrationForm, LoginForm


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for("home"))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'buttstuff':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login not successful dipshit', 'danger')
    return render_template("login.html", title='Login', form=form)
