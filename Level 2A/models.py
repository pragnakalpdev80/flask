from extensions import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)

# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)
#     is_active = db.Column(db.Boolean, default=True)

#     def __repr__(self):
#         return f'<User {self.username}>'

# class Author(db.Model):
#     __tablename__ = 'authors'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True, nullable=False)
#     bio = db.Column(db.String(500))

#     # One-to-Many: One author has many books
#     books = db.relationship('Book', backref='author', cascade='all, delete-orphan')

# class Book(db.Model):
#     __tablename__ = 'books'

#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     price = db.Column(db.Float, nullable=False)

#     # Foreign Key: Links to Author table
#     author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)