from flask import Flask, jsonify, request, Blueprint
from extensions import db, migrate, jwt, bcrypt
from dotenv import load_dotenv
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

    
if __name__ == "__main__":
    app.run(debug=True)