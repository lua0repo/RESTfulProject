from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the Movie model
from models import Movie

# Route to create a new movie
@app.route('/movies', methods=['POST'])
def add_movie():
    data = request.get_json()
    
    title = data.get('title')
    director = data.get('director')
    release_year = data.get('release_year')
    genre = data.get('genre')
    
    if not all([title, director, release_year, genre]):
        return jsonify({"error": "Missing required fields"}), 400
    
    new_movie = Movie(title=title, director=director, release_year=release_year, genre=genre)
    db.session.add(new_movie)
    db.session.commit()
    
    return jsonify({"message": "Movie added successfully", "movie": new_movie.to_dict()}), 201

# Route to get all movies
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies]), 200

# Route to get a movie by its ID
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    return jsonify(movie.to_dict()), 200

# Route to update a movie
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    data = request.get_json()
    movie = Movie.query.get_or_404(movie_id)
    
    movie.title = data.get('title', movie.title)
    movie.director = data.get('director', movie.director)
    movie.release_year = data.get('release_year', movie.release_year)
    movie.genre = data.get('genre', movie.genre)
    
    db.session.commit()
    
    return jsonify({"message": "Movie updated successfully", "movie": movie.to_dict()}), 200

# Route to delete a movie
@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    
    return jsonify({"message": "Movie deleted successfully"}), 200

if __name__ == '__main__':
    # Create the database if it doesn't exist
    db.create_all()
    app.run(debug=True)
