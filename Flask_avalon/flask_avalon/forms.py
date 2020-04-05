from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_avalon.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators =[DataRequired()])

    confirm_password =  PasswordField('Confirm Password',
        validators =[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username taken, be more original')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('email taken, be more original')


class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators =[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class GameStart(FlaskForm):
    password = PasswordField('Password',
        validators = [DataRequired()])

    submit = SubmitField('Enter')
