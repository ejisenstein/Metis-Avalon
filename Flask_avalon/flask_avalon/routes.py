from flask import render_template, url_for, flash, request, redirect, request
from flask_avalon import app, db, bcrypt
from flask_avalon.models import User, TeamVote
from flask_avalon.forms import RegistrationForm, LoginForm, GameStart, TeamBuilderForm, QuestVote
from flask_login import login_user, current_user, logout_user, login_required
from multiprocessing import Value

counter = Value('i', 0)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login not successful dipshit', 'danger')
    return render_template("login.html", title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/gamestatus", methods=['GET', 'POST'])
def gamestatus():
    form = GameStart()
    team_decision = TeamBuilderForm()
    quest_vote = QuestVote()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            flash('Game will now begin', 'success')
            user = User.query.filter_by(email=form.email.data).first()
            user.join_game = True
            db.session.commit()
            out = User.query.filter_by(join_game=True).count()
            query= User.query.filter_by(join_game=True).all()

            return render_template("gamestatus.html", form=form, text=out,
            query=query, team_decision=team_decision, quest_vote=quest_vote)
    return render_template("gamestatus.html", form=form)
