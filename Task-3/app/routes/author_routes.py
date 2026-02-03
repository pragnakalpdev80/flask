from flask import Blueprint, request, jsonify
from app.services.author_service import AuthorService

author_bp = Blueprint('author', __name__)

@author_bp.route('/api/v1/authors', methods=['POST'])
def create_author():
    author, error, status = AuthorService.create_author(request.get_json())
    if error:
        print(error)
        return jsonify({"error": error}), status
    return jsonify({
        "id": author.id,
        "name": author.name,
        "bio": author.bio
    }), status


@author_bp.route("/api/v1/authors/<int:id>", methods=["GET"])
def get_author(id):
    author,all_books, error, status = AuthorService.get_author(id)
    if error:
        return jsonify({"error": error}), status
    return jsonify({
        "id": author.id,
        "name": author.name,
        "bio": author.bio,
        "books": all_books
    }), status


@author_bp.route("/api/v1/authors/<int:id>", methods=["DELETE"])
def delete_author(id):
    success, error, status = AuthorService.delete_author(id)
    if error:
        return jsonify({"error": error}), status
    return jsonify({"message": "Author deleted"}), status

