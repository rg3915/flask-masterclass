from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import routes

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    routes.init_app(app)
    db.init_app(app)

    return app
