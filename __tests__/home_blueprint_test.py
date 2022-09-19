from splinter import Browser
from ward import test

from app import create_app, db
from app.models import Post


# @test('Página principal deve estar online.')
# def _():
#     app = create_app()
#     app.testing = True
#     browser = Browser('flask', app=app)

#     browser.visit('/')
#     assert browser.is_text_present('Olá, Flask!')


@test('Visitante acessa a página principal e vê posts.')
def _():
    app = create_app()
    app.testing = True

    context = app.test_request_context()
    context.push()

    with app.test_client():
        db.create_all()

        post = Post(
            title='Curtindo as férias em Salvador',
            published=True,
            text='text...'
        )
        db.session.add(post)
        db.session.commit()

        browser = Browser('flask', app=app)
        browser.visit('/')

        assert browser.is_text_present('Curtindo as férias em Salvador')

        db.drop_all()
        db.session.remove()
