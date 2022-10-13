from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, StringField, SubmitField


class CategoryForm(FlaskForm):
    name = StringField('Nome')
    submit = SubmitField('Salvar')


class PostForm(FlaskForm):
    title = StringField('Título')
    text = StringField('Texto')
    published = BooleanField('Publicar')
    submit = SubmitField('Salvar')
