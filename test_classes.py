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
    assert m.average_rating == 3.00


def test_make_user():
    m = User(3)
    assert isinstance(m, User)
    assert m.user_id == 3


ratings_dict_by_user = {1: [[345, 5], [546, 3], [765, 4]],
                        2: [[42, 4]],
                        3: [[654, 3], [543, 4]],
                        4: [[545, 4], [234, 4], [333, 5], [654, 5], [333, 5]]}


def test_make_user_ratings():
    m = User(3)
    m.make_ratings(ratings_dict_by_user)
    assert m.rating_list == [[654, 3], [543, 4]]


def test_make_user_average_rating():
    m = User(3)
    m.make_ratings(ratings_dict_by_user)
    m.make_average_rating()
    assert m.average_rating == 3.50


def test_str_movie():
    m = Movie(3)
    m.make_title(movie_names_dict)
    m.make_ratings(movie_ratings_dict)
    m.make_movie_average_rating()
    assert str(m) == "Return of the Jedi is at ID # 3 and has an average\
 rating of 3.0"


def test_str_user():
    u = User(3)
    u.make_ratings(ratings_dict_by_user)
    assert str(u) == "User 3 has made these ratings: (MovieID, rating): \
[[654, 3], [543, 4]]"
