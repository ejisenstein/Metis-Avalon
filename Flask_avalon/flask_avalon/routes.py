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
    logout_user()
    return redirect(url_for('home'))

@app.route("/gamestatus", methods=['GET', 'POST'])
def gamestatus():
    form = GameStart()
    quest_vote = QuestVote()
    sub_team_form = SubmitTeamForm()

    if form.validate_on_submit() and current_user.is_authenticated:
        flash('Game will now begin', 'success')
        # current_user.team_order = team_order[0]
        # team_order.pop(0) #popping out from team order the random num assigned
        current_user.join_game = True
        db.session.commit()
        # res = User.query.order_by(User.team_order).all()
        # out = User.query.filter_by(join_game=True).count()
        joined_players= User.query.filter_by(join_game=True).all()
        init_team_list = random.sample(range(1,6),5)
        order_of_players = User.query.order_by(User.team_order.desc()).all()
        active_players = User.query.filter_by(join_game=True).count()
        # if active_players == num_of_players:
        #     # for ind, player in enumerate(player_outs):
        #     #     player.team_order = init_team_list[ind]
        #     # db.session.commit()
        #     # player_outs = User.query.all()


        #
        # if sub_team_form.validate_on_submit:
        #     # for r in res:
        #     #     if r.team_order != 1:
        #     #         r.team_order -=1
        #     #     else:
        #     #         r.team_order = num_of_players
        #         db.session.commit()
        #         flash('Count of players shifted')
        return render_template("gamestatus.html", form=form,
        order_of_players=order_of_players, active_players=active_players, joined_players=joined_players,
        sub_team_form=sub_team_form, quest_vote=quest_vote)
    return render_template("gamestatus.html", form=form)
