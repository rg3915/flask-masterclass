from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField
)

from app.models import Category


class CategoryForm(FlaskForm):
    name = StringField('Nome')
    submit = SubmitField('Salvar')


class PostForm(FlaskForm):
    title = StringField('Título')
    text = TextAreaField('Texto')
    published = BooleanField('Publicar')
    categories = SelectField('Categorias', coerce=int)
    submit = SubmitField('Salvar')

    def __init__(self):
        super(PostForm, self).__init__()
        self.categories.choices = [
            (c.id, c.name) for c in Category.query.all()
        ]
