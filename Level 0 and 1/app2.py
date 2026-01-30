from flask import *
import uuid

app= Flask(__name__)

# @app.route("/users/<user_id>", methods=["GET"])
# def get_user(user_id):
#     # Validate UUID format
#     try:
#         uuid.UUID(user_id)
#     except ValueError:
#         return jsonify({"error": "Invalid UUID format"}), 400

#     # Proceed with valid UUID
#     user = {"id": user_id, "name": "Alice"}
#     return jsonify(user), 200

# Mock database
users = [
    {"id": "a1b2c3", "name": "Alice"},
    {"id": "d4e5f6", "name": "Bob"}
]

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    # Search for user
    user = next((u for u in users if u['id'] == user_id), None)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200
                                
@app.route("/users", methods=["POST"])
def create_user():
    # Flask automatically returns 400 for malformed JSON if force=False (default)
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    # Proceed with valid data
    return jsonify({"message": "User created"}), 201

@app.route("/users", methods=["GET"])
def get_users():
    try:
        # Simulating file read that might fail
        with open("users.json", "r") as f:
            users = json.load(f)
        return jsonify({"users": users}), 200

    except FileNotFoundError:
        # Log the error internally
        print("ERROR: users.json not found!")

        # Return generic error to client
        return jsonify({"error": "Internal server error"}), 500

    except json.JSONDecodeError:
        print("ERROR: Invalid JSON in users.json")
        return jsonify({"error": "Internal server error"}), 500

if __name__=="__main__":
    app.run(debug=True)