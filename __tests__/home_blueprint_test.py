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


@test('Visitante acessa a página principal e não vê posts não publicados.')
def _(browser=browser):
    post = PostFactory.create(title='Curtindo as férias em Salvador')
    drafts = PostFactory.create_batch(2, published=False)

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)
    assert browser.is_text_not_present(drafts[0].title)
    assert browser.is_text_not_present(drafts[1].title)


@test('Visitante não consegue visualizar posts.')
def _(browser=browser):
    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Nenhum post cadastrado!')
