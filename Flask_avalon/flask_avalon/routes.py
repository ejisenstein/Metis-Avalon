from flask import render_template, url_for, flash, request, redirect, request
from flask_avalon import app, db, bcrypt
from flask_avalon.models import User, TeamVote
from flask_avalon.forms import RegistrationForm, LoginForm, GameStart, SubmitTeamForm, QuestVote
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.sql import select
import random

num_of_players = 5 #Later version will have dynamic playercounts, this is a var placeholder in the meantime


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
    current_user.join_game=False
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))

@app.route("/gamestatus", methods=['GET', 'POST'])
def gamestatus():
    form = GameStart()
    quest_vote = QuestVote()
    sub_team_form = SubmitTeamForm()
    active_players = User.query.filter_by(join_game=True).count()

    if form.validate_on_submit() and current_user.is_authenticated and current_user.join_game==False and active_players < num_of_players:
        flash('You have logged in! Game will begin when rest of party logs in', 'success')
        current_user.join_game = True
        db.session.commit()
        active_players = User.query.filter_by(join_game=True).count()
        order_of_players=0
        joined_player = User.query.filter_by(join_game=True).all()


    elif form.validate_on_submit() and current_user.is_authenticated and current_user.join_game==False and active_players == num_of_players:
        flash ('Game has begun', 'success')
        current_user.join_game = True
        db.session.commit()

        joined_player = User.query.filter_by(join_game=True).all()
        init_team_list = random.sample(range(1,6),5)
        active_players = User.query.filter_by(join_game=True).count()

        for ind, player in enumerate(joined_players):
            player.team_order = init_team_list[ind]
            db.session.commit()
        order_of_players = User.query.order_by(User.team_order.asc()).all()
        return render_template("gamestatus.html", form=form,
        order_of_players=order_of_players,
        active_players=active_players,
        joined_players=joined_players,
        num_of_players=num_of_players)
    return render_template("gamestatus.html", form=form, active_players=active_players, num_of_players=num_of_players)
