from flask import Flask
from extensions import db, migrate
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
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

    return app

if __name__=="__main__":
    app = create_app()
    app.run(debug=True)
