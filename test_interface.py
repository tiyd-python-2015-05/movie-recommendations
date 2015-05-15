from file_open_read import *
from nose.tools import raises
from classes import *
from interface import *

number_movies = 3

movie_names_dict = {1: "Star Wars", 2: "Empire Strikes Back",
                    3: "Return of the Jedi"}

movie_ratings_dict = {1: [[345, 2], [545, 5], [645, 3]],
                     2: [[445, 5], [234, 3], [875, 4]],
                     3: [[534, 4], [222, 3], [265, 2]]}

def test_make_movie_objects_list():
    new_movie_list = make_movie_objects_list(number_movies, movie_names_dict,
                                            movie_ratings_dict)
    assert len(new_movie_list) == 3
    assert new_movie_list[0].movie_title == "Star Wars"
    for i in new_movie_list:
        if i.movie_id == 1:
            ratings = i.movie_rating
    assert ratings == [[345, 2], [545, 5], [645, 3]]
