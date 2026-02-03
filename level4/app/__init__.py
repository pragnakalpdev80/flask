from flask import Flask
from extensions import db, migrate, jwt, ma
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from app_config import Config

def create_app(config_class=Config):
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
    app.register_blueprint(auth_bp)

    return app
