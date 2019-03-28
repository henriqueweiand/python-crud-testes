from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_restless

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/storage.db'
db = SQLAlchemy(app)

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)
