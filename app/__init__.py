from dynaconf import FlaskDynaconf
from flask import Flask


def create_app():
    app = Flask(__name__)

    FlaskDynaconf(app, extensions_list=True)

    return app
