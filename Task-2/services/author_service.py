from models import db, Author, Book

class AuthorService:
    @staticmethod
    def create_author(data):
        if not data or "name" not in data:
            return None, "Name is required", 400

        if Author.query.filter_by(name=data["name"]).first():
            return None, "Author already exists", 400

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
        books= Book.query.filter_by(author_id=author.id).all()
        all_books=[]
        for book in books:
            all_books.append({"id":book.id,"title":book.title,"price":book.price})
        return author,all_books, None, 200
    
    @staticmethod
    def delete_author(author_id):
        author = Author.query.get(author_id)
        if not author:
            return False, "Author not found", 404
        db.session.delete(author)
        db.session.commit()
        return True, None, 200
    @staticmethod
    def get_all():
        books=Book.query.all()
        all_books=[]
        for book in books:
            all_books.append({"id":book.id,"title":book.title,"price":book.price,"author_id":book.author_id})
        return all_books,None,200