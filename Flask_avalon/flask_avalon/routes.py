from flask import render_template, url_for, flash, request, redirect
from flask_avalon import app, db, bcrypt
from flask_avalon.models import User, Vote
from flask_avalon.forms import RegistrationForm, LoginForm
from flask_login import login_user


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created, you can login!", 'success')
        return redirect(url_for("login"))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login not successful dipshit', 'danger')
    return render_template("login.html", title='Login', form=form)
