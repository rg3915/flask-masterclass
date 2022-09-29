from dynaconf import FlaskDynaconf
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    FlaskDynaconf(app, extensions_list=True)

    from app import routes  # para resolver o problema de circular imports

    routes.init_app(app)
    db.init_app(app)

    return app
