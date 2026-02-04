from flask import Flask, jsonify
from app.extensions import db, migrate
from config import TestConfig, DevConfig
from app.routes.author_routes import author_bp
from app.routes.book_routes import book_bp

def create_app(config_class=DevConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(author_bp)
    app.register_blueprint(book_bp)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "This endpoint does not exist"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "error": "Method not allowed for this endpoint"
        }), 405
    
    with app.app_context():
        try:
            db.engine.connect()
            print("="*28+"\n [Connected with Database]\n"+"="*28)
        except Exception as e:
            print(e)

    
    return app
