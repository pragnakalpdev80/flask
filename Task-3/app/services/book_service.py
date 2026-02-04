from app.models.book import Book
from app.models.author import Author
from app.extensions import db

class BookService:
    @staticmethod
    def create_book(data):
        if not data or "title" not in data or "price" not in data:
            return None, "Name or Price is missing", 400
        
        if "author_id" not in data:
            return None, "Author id is required", 400
        if not Author.query.filter_by(id=data["author_id"]).first():
            return None, "Author not exists.",400
        
        book=Book(title=data["title"],
                  price=data["price"],
                  author_id=data["author_id"])
        db.session.add(book)
        db.session.commit()

        return book, None, 201
    
    @staticmethod
    def update_book_price(book_id,data):
        book = Book.query.get(book_id)
        if not book:
            return None, "Book not found",404
        
        if not data or "price" not in data:
            return None, "Price is missing", 400
        
        updated_book= Book.query.filter_by(id=book_id).first()
        if updated_book.price==data["price"]:
            return None, "Please provide updated price",400
        updated_book.price=data["price"]
        db.session.commit()        
        
        return updated_book, None, 200
    
    @staticmethod
    def get_all():
        books=Book.query.filter_by(is_deleted=False).all()
        all_books=[]
        for book in books:
            all_books.append({"id":book.id,"title":book.title,"price":book.price,"author_id":book.author_id})
        return all_books,None,200



    
    
    