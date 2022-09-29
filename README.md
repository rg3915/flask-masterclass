# flask-masterclass

Curso Flask Masterclass com Marcus Pereira


## Este projeto foi feito com:

* [Python 3.10.4](https://www.python.org/)
* [Flask 2.2.0](https://flask.palletsprojects.com/en/2.2.x/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode a aplicação.

```
git clone https://github.com/rg3915/flask-masterclass.git
cd flask-masterclass
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

flask run
flask routes

FLASK_ENV=development flask run  # ou
# FLASK_DEBUG=development flask run
```

Ou você pode usar o [python-dotenv](https://pypi.org/project/python-dotenv/) para gerenciar as variáveis de ambiente.

### Testes

Para rodar os testes digite

```
ward
```

### Banco de dados

Vamos usar o [flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x).


### Shell

```
flask shell
```

```python
from app import db
from app.models import Post

db.create_all()

post = Post(
    title='Curtindo as férias em Salvador',
    published=True,
    text='text...'
)
db.session.add(post)
db.session.commit()

Post.query.all()
```

### Acessando o sqlite

```
sqlite3 app/betravel.sqlite

.tables

.schema

.headers on

SELECT * FROM post;
```

