import os
from dotenv import load_dotenv


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    load_dotenv()
    SQLALCHEMY_DATABASE_URI=os.getenv('DB_URL')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False