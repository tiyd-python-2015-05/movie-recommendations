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

number_users = 4

ratings_dict_by_user = {1: [[345, 5], [546, 3], [765, 4]],
                        2: [[42, 4]],
                        3: [[654, 3], [543, 4]],
                        4: [[545, 4], [234, 4], [333, 5], [654, 5], [333, 5]]}


def test_make_user_objects_list():
    new_user_list = make_user_objects_list(number_users, ratings_dict_by_user)
    assert len(new_user_list) == 4
    assert new_user_list[0].user_id == 1
    for i in new_user_list:
        if i.user_id == 1:
            ratings = i.rating_list
    assert ratings == [[345, 5], [546, 3], [765, 4]]

def test_make_top_list():
    new_movie_list = make_movie_objects_list(number_movies, movie_names_dict,
                                                movie_ratings_dict)
    assert len(new_movie_list) == 3
    assert (top_movies(new_movie_list))[0].movie_title == "Empire Strikes Back"
    assert (top_movies(new_movie_list))[1].movie_title == "Star Wars"
