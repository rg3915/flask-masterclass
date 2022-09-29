# from faker import Faker
from flask import url_for
from ward import test

from __tests__.factories.post_factory import PostFactory
from __tests__.fixtures import browser

# from app import db
# from app.models import Post


@test('Página principal deve estar online.')
def _(browser=browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Olá, Flask!')


@test('Visitante acessa a página principal e vê posts.')
def _(browser=browser):
    # post = Post(
    #     title=faker.paragraph(),
    #     published=True,
    #     text='text...'
    # )
    post = PostFactory.create()

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)


@test('Visitante não consegue visualizar posts.')
def _(browser=browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Nenhum post cadastrado!')
