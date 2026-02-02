from flask_marshmallow import Marshmallow
from marshmallow import ValidationError
from models.book import Book

ma = Marshmallow()

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True  

