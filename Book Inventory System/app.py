from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(
        title=data['title'],
        author=data['author'],
        genre=data['genre'],
        published_year=data['published_year']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully!'}), 201

# Route to list all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'published_year': book.published_year
        }
        for book in books
    ]
    return jsonify({'books': books_list})

# Route to get a specific book by ID
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'genre': book.genre,
        'published_year': book.published_year
    })

# Route to update a book's details
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()
    
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.genre = data.get('genre', book.genre)
    book.published_year = data.get('published_year', book.published_year)

    db.session.commit()
    return jsonify({'message': 'Book updated successfully!'})

# Route to delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully!'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
