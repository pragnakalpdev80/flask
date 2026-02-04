from app.extensions import db
from app.models.author import Author
from app.models.book import Book

def register_commands(app):
    @app.cli.command('seed-db')
    def seed_data():
        
        if Author.query.filter_by(id=1).first():
            return False
        if Author.query.filter_by(id=2).first():
            return False
        if Author.query.filter_by(name="author1").first():
            return False
        if Author.query.filter_by(name="author2").first():
            return False
        
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