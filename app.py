from flask import Flask, Blueprint


def create_app():
    app = Flask(__name__)

    home = Blueprint('home', __name__)

    @app.route('/')
    def index():
        return "Olá, Flask!"

    app.register_blueprint(home)

    return app
