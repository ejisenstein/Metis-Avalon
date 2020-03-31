from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = '93548cc0fde27fd878cb9aab95033646'
db = SQLAlchemy(app)

from flask_avalon import routes
