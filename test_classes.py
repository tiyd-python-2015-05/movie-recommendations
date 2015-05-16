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
                        4: [[545, 4], [234, 4], [333, 5], [654, 5], [334, 5]]}


def test_make_user_ratings():
    m = User(3)
    m.make_ratings(ratings_dict_by_user)
    assert m.rating_list == [[654, 3], [543, 4]]
    assert m.user_sim_dict == {}


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


def test_movies_reviewed():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user)
    u.make_ratings(ratings_dict_by_user)
    t.movies_reviewed()
    u.movies_reviewed()
    assert t.movies_list == [654, 543]
    assert u.movies_list == [545, 234, 333, 654, 334]

def test_common_user_reviews():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user)
    u.make_ratings(ratings_dict_by_user)
    t.movies_reviewed()
    u.movies_reviewed()
    assert t.make_common_reviews(u) == [654]

def test_uncommon_user_reviews():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user)
    u.make_ratings(ratings_dict_by_user)
    t.movies_reviewed()
    u.movies_reviewed()
    assert t.make_uncommon_reviews(u) == [545, 234, 333, 334]

def test_make_ratings_dict():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user)
    u.make_ratings(ratings_dict_by_user)
    t.make_ratings_dict()
    u.make_ratings_dict()
    assert t.ratings_dict == {654: 3, 543: 4}
    assert u.ratings_dict == {545: 4, 234: 4, 333: 5, 654: 5, 334: 5}

def test_make_user_other_vector():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user)
    u.make_ratings(ratings_dict_by_user)
    t.make_ratings_dict()
    u.make_ratings_dict()
    t.movies_reviewed()
    u.movies_reviewed()
    assert t.make_ratings_vectors(u) == ([3], [5])


ratings_dict_by_user2 =  {3: [[654, 3], [543, 4], [333, 5], [334, 4]],
                        4: [[545, 4], [234, 4], [333, 5], [654, 5], [334, 5]]}

def test_make_user_other_vector2():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user2)
    u.make_ratings(ratings_dict_by_user2)
    t.make_ratings_dict()
    u.make_ratings_dict()
    t.movies_reviewed()
    u.movies_reviewed()
    assert t.make_ratings_vectors(u) == ([3, 5, 4], [5, 5, 5])

v1 = []
v2 = [1, 2, 3]
v3 = [1, 2, 3, 4, 5]
v4 = [1, 2, 3, 4, 5]
v5 = [5, 4, 3, 2, 1]
v6 = [2, 2, 3, 4, 2]
v7 = [5, 2, 1, 4, 2]
v8 = []

@raises(ShapeException)
def test_calculate_similarity_exception():
    calculate_similarity(v3, v2)

def test_calculate_similarity_empty_vector():
    assert calculate_similarity(v1, v8) == 0
    assert 0 <= calculate_similarity(v6, v7) <= 1
    assert 0 <= calculate_similarity(v4, v5) == .137

ratings_dict_by_user3 =  {3: [[654, 3], [543, 4], [333, 5], [334, 4], [555, 5]],
                        4: [[545, 4], [234, 4], [333, 5], [654, 5], [334, 5], [555, 5]]}

def test_create_user_sim_scores():
    t = User(3)
    u = User(4)
    t.make_ratings(ratings_dict_by_user3)
    u.make_ratings(ratings_dict_by_user3)
    t.make_ratings_dict()
    u.make_ratings_dict()
    t.movies_reviewed()
    u.movies_reviewed()
    assert t.create_similarity_score(u) == .309
    assert t.user_sim_dict[4] == .309
