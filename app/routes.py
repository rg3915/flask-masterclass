from app.blueprints.categories_blueprint import category
from app.blueprints.home_blueprint import home
from app.blueprints.posts_blueprint import post


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(post)
    app.register_blueprint(category)
