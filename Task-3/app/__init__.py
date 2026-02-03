from flask import Flask
from app.extensions import db, migrate
from config import TestConfig
from app.routes.author_routes import author_bp
from app.routes.book_routes import book_bp

def create_app(config_class=TestConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(author_bp)
    app.register_blueprint(book_bp)

    with app.app_context():
        try:
            db.engine.connect()
            print("="*28+"\n [Connected with Database]\n"+"="*28)
        except Exception as e:
            print(e)

    
    return app
