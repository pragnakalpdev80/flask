from app.models.book import Book
from app.models.author import Author
from app.extensions import db
from sqlalchemy import and_

class AuthorService:
    @staticmethod
    def create_author(data):
        if not data or "name" not in data:
            return None, "Name is required", 400

        author=Author.query.filter_by(name=data["name"]).first()
        if author:
            if Author.query.filter_by(name=data["name"],is_deleted=False).first():
                return None, "Author already exists", 404 
            author.name=data["name"]
            author.bio=data.get("bio") 
            author.is_deleted=False
        else:
            author = Author(
                name=data["name"],
                bio=data.get("bio")
            )
            db.session.add(author)
        db.session.commit()
        return author, None, 201

    @staticmethod
    def get_author(author_id):
        author = Author.query.get(author_id)
        
        if not author:
            return None,None, "Author not found", 404
        if Author.query.filter_by(id=author_id,is_deleted=True).first():
            return None,None, "Author not found.", 404
        books= Book.query.filter_by(author_id=author.id,is_deleted=False).all()
        all_books=[]
        for book in books:
            all_books.append({"id":book.id,"title":book.title,"price":book.price})
        return author,all_books, None, 200
    
    @staticmethod
    def delete_author(author_id):
        author = Author.query.get(author_id)
        if not author:
            return False, "Author not found", 404
        delete_author= Author.query.filter_by(id=author_id).first()
        delete_author.is_deleted=True
        delete_books=Book.query.filter_by(author_id=author_id).update({'is_deleted':True})
        db.session.commit()
        return True, None, 200
    
    