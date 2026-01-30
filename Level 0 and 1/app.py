from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, Flask!"})

@app.route("/books", methods=["GET"])
def get_books():
    books = [
        {"id": 1, "title": "Flask Guide", "author": "John Doe"},
        {"id": 2, "title": "Python Basics", "author": "Jane Smith"}
    ]
    return jsonify({"books": books}), 200

@app.route("/books", methods=["POST"])
def create_book():
    return jsonify({"message": "Create a book"}), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book_full(book_id):
    data = request.get_json()

    # PUT requires ALL fields to be present
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "PUT requires title AND author"}), 400

    # In a real app, check if book exists first
    # If not found: return 404

    # Replace the entire resource
    updated_book = {
        "id": book_id,
        "title": data['title'],
        "author": data['author']
    }
    # get_books().books.append(updated_book)
    return jsonify({"message": "Book replaced", "book": updated_book}), 200

@app.route("/books/<int:book_id>", methods=["PATCH"])
def update_book_partial(book_id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # In a real app, fetch existing book from DB
    existing_book = {
        "id": book_id,
        "title": "Original Title",
        "author": "Original Author",
        "year": 2020
    }

    # Check if book exists
    # if not found: return 404

    # Update only the fields that were sent
    if 'title' in data:
        existing_book['title'] = data['title']
    if 'author' in data:
        existing_book['author'] = data['author']
    if 'year' in data:
        existing_book['year'] = data['year']

    return jsonify({"message": "Book updated", "book": existing_book}), 200

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    # In a real app, check if book exists
    # If not found: return 404

    # Delete from database
    # db.session.delete(book)
    # db.session.commit()

    return jsonify({"message": "Book deleted successfully"}), 200

# @app.route("/books/<int:book_id>", methods=["DELETE"])
# def delete_book(book_id):
#     # Delete logic here
#     return '', 204  # No content

@app.route("/ping")
def ping():
    return jsonify({"pong":True})

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    result = data["x"] + data["y"]  # Error if x or y is string
    return jsonify({"result": result})

@app.route("/process")
def process_data():
    data = request.get_json()
    print(f"DEBUG: Received data: {data}")  # Check what you received

    result = data.get("value", 0) * 2
    print(f"DEBUG: Calculated result: {result}")  # Check calculation

    return jsonify({"result": result})

@app.route("/users/<int:user_id>")
def get_user(user_id):
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    user = next((u for u in users if u["id"] == user_id), None)
    # What if user is None?
    return jsonify({"name": user["name"]})  # Error if user is None

@app.route("/users", methods=["GET"])
def list_users():
    # request.args is a dictionary-like object
    page = request.args.get("page", 1, type=int)
    role = request.args.get("role")
    role2 = request.args.get("isadmin")
    return jsonify({"page": page, "filter_role": [role,role2]})

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    # Scenario 1: No JSON body
    if not data:
        return jsonify({"error": "Request body is required"}), 400

    # Scenario 2: Missing required fields
    if 'name' not in data:
        return jsonify({"error": "Missing 'name' field"}), 400

    if 'email' not in data:
        return jsonify({"error": "Missing 'email' field"}), 400
    
    if 'age' not in data:
        return jsonify({"error": "Missing 'age' field"}), 400
    # Scenario 3: Invalid data type
    if not isinstance(data.get('age'), int):
        return jsonify({"error": "Age must be an integer"}), 400

    # Success
    return jsonify({"message": "User created"}), 201

@app.route("/broken")
def broken_endpoint():
    # This will cause an error
    numbers = [1, 2, 3]
    result = numbers[10]  # IndexError: list index out of range
    return jsonify({"result": result})

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    if not data or "item" not in data:
        # 400 Bad Request
        return jsonify({"error": "Missing 'item' field"}), 400

    return jsonify({"id": 123, "status": "pending"}), 201

if __name__ == "__main__":
    # if not app.debug:
    #     logging.basicConfig(filename='app.log', level=logging.ERROR)
    app.run(debug=True)