from flask import url_for
from ward import test

from __tests__.fixtures import browser
from app.models import Post


@test('Usuário cadastra post.', tags=['posts'])
def _(browser=browser):
    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Cadastrar postagem').click()
    browser.fill('title', 'Passando as férias em Salvador')
    browser.fill('text', 'lorem ipsum...')
    browser.check('published')
    browser.find_by_value('Salvar').click()

    assert browser.url == url_for('home.index')
    assert browser.is_text_present('Post publicado com sucesso')
    assert Post.query.first().title == 'Passando as férias em Salvador'
    assert Post.query.count() == 1
