from flask import request, Blueprint, jsonify, abort, Response
from app.article.article_model import Article
from app.main import db

article = Blueprint('article', __name__)


@article.route("/article/all")
def get_articles():
    articles_list = Article.query.all()
    return jsonify({
        'data': [article_in_list.serialized for article_in_list in articles_list]
    })


@article.route("/article/<int:id_article>")
def get_article(id_article):
    article_from_query = Article.query.get(id_article)
    if article_from_query is None:
        abort(404)
    return jsonify({
        'data': [article_from_query.serialized]
    })


@article.route("/article/create", methods=["POST"])
def create_article():
    article_request = assign_data_to_article(request.get_json())
    article_request.save()
    return jsonify({
        'data': [article_request.serialized]
    })


@article.route("/article/edit/<int:id_article>", methods=["PUT"])
def edit_article(id_article):
    article_edit = Article.query.get(id_article)
    print(article_edit)
    if article_edit is None:
        abort(404)
    update_article(article_edit, request.get_json())
    db.session.commit()
    return Response(status=200)


@article.route("/article/delete/<int:id_article>", methods=["DELETE"])
def delete_article(id_article):
    article_delete = Article.query.get(id_article)
    if article_delete is None:
        abort(404)
    db.session.delete(article_delete)
    db.session.commit()
    return Response(status=200)


def assign_data_to_article(data):
    new_article = Article(name=data['name'], price=data['price'], description=data['description'], stock=data['stock'],
                          category_id=data['category_id'])
    return new_article


def update_article(article_edit, data):
    article_edit.name = data['name']
    article_edit.price = data['price']
    article_edit.description = data['description']
    article_edit.stock = data['stock']
    article_edit.category_id = data['category_id']
