from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# from app import app

jwt = JWTManager()
bcrypt = Bcrypt()
db=SQLAlchemy()
migrate=Migrate()
