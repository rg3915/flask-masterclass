from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)

    @app.shell_context_processor
    def load_context_processor():
        from app.models import Post  # corrige circular import

        return dict(
            app=app,
            db=db,
            Post=Post,
        )
