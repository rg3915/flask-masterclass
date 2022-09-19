from ward import test

from __tests__.fixtures import browser
from app import db
from app.models import Post


@test('Página principal deve estar online.')
def _(browser=browser):
    browser.visit('/')

    assert browser.is_text_present('Olá, Flask!')


@test('Visitante acessa a página principal e vê posts.')
def _(browser=browser):
    post = Post(
        title='Curtindo as férias em Salvador',
        published=True,
        text='text...'
    )
    db.session.add(post)
    db.session.commit()

    browser.visit('/')

    assert browser.is_text_present('Curtindo as férias em Salvador')
