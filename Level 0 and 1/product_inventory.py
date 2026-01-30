from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    # Error 1: Validate product_id is positive
    if product_id <= 0:
        return jsonify({"error": "Invalid product ID"}), 400

    # Error 2: Load products from file
    try:
        with open("inventory.json", "r") as f:
            data = json.load(f)
            products = data.get("products", [])
    except FileNotFoundError:
        return jsonify({"error": "Internal server error"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Internal server error"}), 500

    # Error 3: Product not found
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Success
    return jsonify(product), 200


@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    # Error 1: No data
    if not data:
        return jsonify({"error": "Request body required"}), 400

    # Error 2: Missing required fields
    if 'name' not in data or 'price' not in data:
        return jsonify({"error": "Missing name or price"}), 400

    # Error 3: Invalid data type
    if not isinstance(data['price'], (int, float)) or data['price'] < 0:
        return jsonify({"error": "Price must be a positive number"}), 400

    # Success - create product
    new_product = {
        "id": 123,  # Would be generated
        "name": data['name'],
        "price": data['price']
    }
    return jsonify(new_product), 201

@app.route("/items", methods=["GET"])
def list_items():
    page = request.args.get("page", 1, type=int)
    page_size = request.args.get("page_size", 20, type=int)

    # pretend this comes from your DB
    items = [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"},
    ]

    return jsonify({
        "items": items,
        "page": page,
        "page_size": page_size,
        "total": len(items),
    })

if __name__=="__main__":
    app.run(debug=True)