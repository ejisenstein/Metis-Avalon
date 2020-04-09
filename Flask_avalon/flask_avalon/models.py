from flask_avalon import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable = False)
    join_game = db.Column(db.Boolean, default=False, nullable=False)
    votes = db.relationship('Vote', backref='author', lazy=True)
    character = db.relationship('Character', backref='author', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Vote('{self.vote}')"


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    good = db.Column(db.Boolean, nullable=False)
    special = db.Column(db.Boolean, nullable=False)
    team_vote = db.Column(db.Boolean, nullable=False)
    quest_vote = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Character('{self.good}')"
