from flask import Flask
from app.extensions import db, migrate, jwt, bcrypt
from dotenv import load_dotenv
import os
from routes.auth_routes import auth_bp

load_dotenv()
def create_app():
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

    app.register_blueprint(auth_bp)

    return app

# @app.route('/register', methods=['POST'])
# def register():
#     json_data = request.get_json()
#     if not json_data:
#         return jsonify({"error": "No input data provided"}), 400

#     try:
#         data = user_schema.load(json_data)

#         user = AuthService.register_user(
#             username=data.username,
#             email=data.email,
#             password_hash=data.password_hash
#         )
#         return user_schema.dump(user), 201
#     except ValidationError as err:
#         return jsonify(err.messages), 400
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()

#     if not data:
#         return jsonify({"error": "No input data provided"}), 400

#     try:
#         result = AuthService.login_user(
#             email=data['email'],
#             password=data['password']
#         )
#         return jsonify(result), 200

#     except Exception as e:
#         return jsonify({"error": str(e)}), 401

# @app.route('/secret', methods=['GET'])
# @jwt_required()
# def secret_route():
#     current_user = get_jwt_identity()
#     return jsonify({
#         "message": "Top Secret",
#         "user": current_user
#     }), 200

if __name__ == "__main__":
    app=create_app
    app.run(debug=True)