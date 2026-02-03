from models.users import User, db
from extensions import bcrypt
from flask_jwt_extended import create_access_token
from errors import AppError

class AuthService:
    @staticmethod
    def register_user(username, email, password_hash):
        if User.query.filter_by(email=email).first():
            raise AppError("Email already exists", 400)

        password_hash = bcrypt.generate_password_hash(password_hash).decode('utf-8')

        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def login_user(email, password):
        user = User.query.filter_by(email=email).first()

        if not user or not bcrypt.check_password_hash(user.password_hash, password):
            raise AppError("Invalid credentials", 401)

        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token, "user_id": user.id}
