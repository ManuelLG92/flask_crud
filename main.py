import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import config
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from app.article.article_controller import article
from app.category.category_controller import category

app.register_blueprint(article)
app.register_blueprint(category)


# create_category()
# create_articles()

@app.route('/')
def hello_world():
    return 'Hello, World!'
