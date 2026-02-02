from flask_marshmallow import Marshmallow
from marshmallow import ValidationError
from models import Book

ma = Marshmallow()

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True  

book_schema = BookSchema()
books_schema = BookSchema(many=True)