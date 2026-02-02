from flask import Flask
from extensions import db, migrate
from flask import Flask, jsonify
from models.users import User
from schemas.users_schema import UserSchema
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Recommended

db.init_app(app)
migrate.init_app(app, db)

with app.app_context():
    try:
        db.engine.connect()
        print("Connected")
    except Exception as e:
        print(e)

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        result = users_schema.dump(users)
        return jsonify(result), 200
    except:
        return jsonify({"error": "Internal Server Error"}),500

if __name__=="__main__":
    app.run(debug=True)
