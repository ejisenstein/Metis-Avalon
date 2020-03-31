from flask_avalon import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    votes = db.relationship('Vote', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}')"

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vote = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Vote('{self.vote}')"
