from flask import Flask, Blueprint
import routes


def create_app():
    app = Flask(__name__)

    home = Blueprint('home', __name__)

    routes.init_app(home)

    app.register_blueprint(home)

    return app
