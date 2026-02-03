from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    user = AuthService.register_user(
        data['username'], data['email'], data['password']
    )
    return jsonify({"message": "User registered","user":user}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    result = AuthService.login_user(data['email'], data['password'])
    return jsonify(result), 200