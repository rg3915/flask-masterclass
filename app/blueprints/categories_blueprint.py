from flask import Blueprint, render_template

from app.models import Post

category = Blueprint('categories', __name__, url_prefix='/categories')


@category.get('/new')
def new():
    return render_template('categories/new.html')
