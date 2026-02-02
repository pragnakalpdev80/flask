from models.book import Book
from extensions import db

class BookService:
    @staticmethod
    def add_book(title, author, isbn):
        existing=Book.query.filter_by(isbn=isbn).first()
        if existing:
            return None, "Book with this ISBN already exists"
        
        book=Book(title=title,author=author, isbn=isbn)
        db.session.add(book)
        db.session.commit()

        return book, None
    
    @staticmethod
    def get_books_by_author(author):
        return Book.query.filter_by(author=author).all()