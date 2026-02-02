from flask import Flask, jsonify, request
from extensions import db, migrate
from models.users import User
from models.book import Book
from schemas.users_schema import UserSchema
from schemas.book_schema import BookSchema
from services.book_service import BookService
from marshmallow import ValidationError
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    try:
        db.engine.connect()
        print("Connected")
    except Exception as e:
        print(e)

user_schema = UserSchema()
users_schema = UserSchema(many=True)
book_schema = BookSchema()
books_schema = BookSchema(many=True)

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result), 200
    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500

@app.route('/books', methods=['POST'])
def create_book():
    json_data = request.get_json()

    if not json_data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        data = book_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    book, error = BookService.add_book(
        title=data.title,
        author=data.author,
        isbn=data.isbn
    )

    if error:
        return jsonify({"error": error}), 400

    return book_schema.dump(book), 201

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books=Book.query.all()
        result = books_schema.dump(books)
        return jsonify(result), 200

    except Exception:
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)