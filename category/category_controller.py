from flask import request, Blueprint, jsonify
from app.category.category_model import Category

category = Blueprint('category', __name__)

@category.route("/category/all")
def get_categoriess():
    categories_list = Category.query.all()
    return jsonify({
        'data': [category_list.serialized for category_list in categories_list]
    })

@category.route("/category/<int:id_category>")
def get_category(id_category):
    category_from_query = category.query.get(id_category)
    if category_from_query is None:
        abort(404)
    return jsonify({
        'data': [category_from_query.serialized]
    })


@category.route("/category/create", methods=["POST"])
def create_category():
    category_request = assign_data_to_category(request.get_json())
    category_request.save()
    return jsonify({
        'data': [category_request.serialized]
    })


@category.route("/category/edit/<int:id_category>", methods=["PUT"])
def edit_category(id_category):
    category_edit = category.query.get(id_category)
    print(category_edit)
    if category_edit is None:
        abort(404)
    update_category(category_edit, request.get_json())
    db.session.commit()
    return Response(status=200)


@category.route("/category/delete/<int:id_category>", methods=["DELETE"])
def delete_category(id_category):
    category_delete = category.query.get(id_category)
    if category_delete is None:
        abort(404)
    db.session.delete(category_delete)
    db.session.commit()
    return Response(status=200)


def assign_data_to_category(data):
    new_category = Category(name=data['name'])
    return new_category


def update_category(category_edit, data):
    category_edit.name = data['name']

