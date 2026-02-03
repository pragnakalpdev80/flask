from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.services.author_service import AuthorService

book_bp= Blueprint('book', __name__)


@book_bp.route("/api/v1/books", methods=["POST"])
def create_book():
    book, error, status = BookService.create_book(request.get_json())
    if error:
        return jsonify({"error": error}), status
    return jsonify({
        "id": book.id,
        "title": book.title,
        "price": book.price,
        "author_id": book.author_id
    }), status
@book_bp.route("/api/v1/books/<int:id>", methods=["PATCH"])
def update_book_price(id):
    book, error, status = BookService.update_book_price(id, request.get_json())
    if error:
        return jsonify({"error": error}), status
    return jsonify({
        "id": book.id,
        "title": book.title,
        "price": book.price
    }), status

@book_bp.route('/api/v1/books', methods=['GET'])
def get_all_books():
    books,error,status=AuthorService.get_all()
    if error:
        return jsonify({"error": error}), status
    return jsonify(books),status