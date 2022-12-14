from flask import Blueprint, flash, redirect, render_template, url_for

from app.extensions import db
from app.forms import PostForm
from app.models import Post

post = Blueprint('posts', __name__, url_prefix='/posts')


@post.get('/<id>')
def show(id):
    post = Post.query.get(id)
    return render_template('posts/show.html', post=post)


@post.get('/new')
def new():
    form = PostForm()
    return render_template('posts/new.html', form=form)


@post.post('/')
def create():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            text=form.text.data,
            published=form.published.data,
            category_id=form.categories.data,
        )
        db.session.add(post)
        db.session.commit()

        flash('Post publicado com sucesso')
        return redirect(url_for('home.index'))

    return render_template('posts/new.html', form=form)
