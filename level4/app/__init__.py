from flask import Flask
from app.extensions import db, migrate, jwt, ma
from app.routes.user_routes import user_bp
from config import TestConfig

def create_app(config_class=TestConfig):
    app = Flask(__name__)

    # 1. Load Configuration
    app.config.from_object(config_class)

    # 2. Init Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    # 3. Register Blueprints
    app.register_blueprint(user_bp)

    with app.app_context():
        try:
            db.engine.connect()
            print("="*28+"\n [Connected with Database]\n"+"="*28)
        except Exception as e:
            print(e)

    
    return app
