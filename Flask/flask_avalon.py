from flask import Flask, redirect, url_for, render_template, request, session, flash, redirect
from forms import RegistrationForm, LoginForm

#from datetime import timedelta
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '93548cc0fde27fd878cb9aab95033646'

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


if __name__ == "__main__":
    app.run(debug=True)
