from flask import Blueprint, jsonify

# Define the blueprint
user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify({"users": []})

@user_bp.route("/<int:id>", methods=["GET"])
def get_user(id):
    return jsonify({"id": id})