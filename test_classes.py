from file_open_read import *
from classes import *
from nose.tools import raises

movie_names_dict = {1: "Star Wars", 2: "Empire Strikes Back",
                    3: "Return of the Jedi"}

movie_ratings_dict = {1: [[345, 2], [545, 5], [645, 3]],
                     2: [[445, 5], [234, 3], [875, 4]],
                     3: [[534, 4], [222, 3], [265, 2]]}


def test_movie_names_dict():
    m = Movie(3)
    m.make_title(movie_names_dict)
    assert m.movie_title == "Return of the Jedi"

def test_movie_ratings_dict():
    m = Movie(3)
    m.make_ratings(movie_ratings_dict)
    assert m.movie_rating == [[534, 4], [222, 3], [265, 2]]

def test_movie_average_review():
    m = Movie(3)
    m.make_ratings(movie_ratings_dict)
    assert m.movie_rating == [[534, 4], [222, 3], [265, 2]]
    m.make_movie_average_rating()
    assert m.average_rating == 3.0
