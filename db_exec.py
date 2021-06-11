from app.main import db
from app.article.article_model import Article
from app.category.category_model import Category


def create_tables():
    db.create_all()


def drop_db():
    db.drop_all()


def create_category():
    cat = Category(name="test")
    cat.save()


def create_articles():
    art = Article(name="play", price=20, description="short description", stock=1, category_id=1)
    art.save()
    art2 = Article(name="two", price=200, description="short description 2", stock=2, category_id=1)
    art2.save()
