# para instalar: pip install Flask
from flask import Flask, jsonify
# para instalar: pip install Flask-Cors
from flask_cors import CORS


app = Flask(__name__)

CORS(app)

class Movies:
    def __init__(self,id, title, release_year, adult=False):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.adult = adult


# Datos de ejemplo

movies = [
    Movies(1, "Toy Story", 1995),
    Movies(2, "Jumanji", 1996),
    Movies(3, "Grumpier Old Men", 1995, True)
]
print(movies)


@app.route('/')
def principal():
    return "Hola mundo, que tal?:)"
@app.route('/movies', methods=['GET'])
def get_movies():
    """
    Recupera todas las peliculas de la lista de ejemplo.
    """
    movies_list = []
    for movie in movies:
        peli = {
            "id": movie.id,
            "title": movie.title,
            "release_year": movie.release_year,
            "adult": movie.adult
        }
        movies_list.append(peli)

    return jsonify(movies_list)  # devuelve la lista de movies_list


if __name__ == '__main__':
    app.run(debug=True)