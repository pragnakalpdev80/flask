from extensions import db
from app.models.author import Author
from app.models.book import Book

def seed_data():

    author = [Author(
            name="author1",
            bio="author1 is Harry Potter Book Writer"),
            Author(
            name="author2",
            bio="author2 is Indian Book Writer")]
    db.session.add_all(author)
    db.session.commit()

    book=[Book(title="Harry Potter 1",price=200,author_id=1),
          Book(title="Harry Potter 2",price=200,author_id=1),
          Book(title="Harry Potter 3",price=200,author_id=1),
          Book(title="Stranger Things 1",price=200,author_id=1),
          Book(title="Stranger Things 2",price=200,author_id=1)]
    db.session.add_all(book)
    db.session.commit()