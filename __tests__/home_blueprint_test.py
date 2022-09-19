from splinter import Browser
from ward import test

from app import create_app


@test('Página principal deve estar online.')
def _():
    app = create_app()
    app.testing = True
    browser = Browser('flask', app=app)

    browser.visit('/')
    assert browser.is_text_present('Olá, Flask!')
