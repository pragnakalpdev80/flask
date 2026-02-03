from flask import Flask, jsonify, request
from flask_migrate import Migrate
from services.author_service import AuthorService
from services.book_service import BookService
from dotenv import load_dotenv
import os
from extensions import db

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DB_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "This endpoint does not exist"
    }), 404

@app.errorhandler(405)
def wrong_method(error):
    return jsonify({
        "error": "Use different method"
    }), 405

@app.route("/authors", methods=["POST"])
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

@app.route("/books", methods=["POST"])
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

@app.route("/authors/<int:id>", methods=["GET"])
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

@app.route("/books/<int:id>", methods=["PATCH"])
def update_book_price(id):
    book, error, status = BookService.update_book_price(id, request.get_json())
    if error:
        return jsonify({"error": error}), status
    return jsonify({
        "id": book.id,
        "title": book.title,
        "price": book.price
    }), status

@app.route("/authors/<int:id>", methods=["DELETE"])
def delete_author(id):
    success, error, status = AuthorService.delete_author(id)
    if error:
        return jsonify({"error": error}), status
    return jsonify({"message": "Author deleted"}), status

@app.route('/books', methods=['GET'])
def get_all_books():
    books,error,status=AuthorService.get_all()
    return jsonify(books),status

if __name__ == "__main__":
    app.run(debug=True)