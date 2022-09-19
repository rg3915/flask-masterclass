from flask import Blueprint

from app.models import Post

home = Blueprint('home', __name__)


@home.route('/')
def index():
    post = Post.query.first()
    return post.title
