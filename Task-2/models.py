from extensions import db

class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    bio = db.Column(db.String(500))

    # One-to-Many: One author has many books
    books = db.relationship('Book', backref='author', cascade='all, delete-orphan')

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    # Foreign Key: Links to Author table
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)