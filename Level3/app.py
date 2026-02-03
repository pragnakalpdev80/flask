from flask import Flask, jsonify, request, Blueprint
from extensions import db, migrate, jwt, bcrypt
from models.users import User
from schemas.users_schema import UserSchema
from dotenv import load_dotenv
from marshmallow import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import AuthService
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

jwt.init_app(app)
bcrypt.init_app(app)
db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    try:
        db.engine.connect()
        print("="*28+"\n [Connected with Database]\n"+"="*28)
    except Exception as e:
        print(e)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

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

@app.route('/register', methods=['POST'])
def register():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        data = user_schema.load(json_data)

        user = AuthService.register_user(
            username=data.username,
            email=data.email,
            password_hash=data.password_hash
        )
        return user_schema.dump(user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        result = AuthService.login_user(
            email=data['email'],
            password=data['password']
        )
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 401

@app.route('/secret', methods=['GET'])
@jwt_required()
def secret_route():
    current_user = get_jwt_identity()
    return jsonify({
        "message": "Top Secret",
        "user": current_user
    }), 200

if __name__ == "__main__":
    app.run(debug=True)