from open_file_read import *
from Movie import *
from nose.tools import raises

sample_data_list = [['196', '242', '3', '881250949'], ['186', '302', '3', '891717742'], \
['22', '377', '1', '878887116'], ['244', '51', '2', '880606923'], \
['166', '346', '1', '886397596'], ['166', '250', '3', '886397596'], \
['22', '346', '2', '880606923']]

sample_item_list = [['1', 'Toy Story (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', \
'0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', \
'0', '0', '0', '0', '0', '0', '0'], \
['2', 'GoldenEye (1995)', \
'01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?GoldenEye%20(1995)', \
'0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', \
'0', '1', '0', '0'], \
['3', 'Four Rooms (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)', '0', '0', '0', '0', \
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], \
['4', 'Get Shorty (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Get%20Shorty%20(1995)', '0', '1', '0', '0', \
'0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], \
['5', 'Copycat (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Copycat%20(1995)', '0', '0', '0', '0', '0', \
'0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0']]

movie_names_dict = {1: "StarWars", 2: "Pig", 3: "ToyStory", 4: "RainMan"}

movie_id_dict = {1:[[25, 3], [253, 2], [255, 3], [210, 2], [12, 3], [10, 5]]}

def test_movie_title():
    m = Movie(1)
    p = Movie(2)
    m.movie_title(movie_names_dict)
    assert m.movie_title == "StarWars"
    # assert p.movie_title(movie_names_dict) == "Pig"

def test_movie_user_ratings():
    m = Movie(1)
    m.movie_ratings_and_average(movie_id_dict)
    assert m.movie_rating == [[25, 3], [253, 2], [255, 3], [210, 2], [12, 3], \
                             [10, 5]]

def test_movie_average_rating():
    m = Movie(1)
    m.movie_ratings_and_average(movie_id_dict)
    assert m.average_rating == 3

def test_user_class():
    m = User(3)
    assert m.user_id == 3

user_id_dict = {1:[[250, 3], [253, 2], [255, 3], [210, 2], [12, 3], [10, 5]],\
                2:[[250, 1], [253, 1], [55, 4], [10, 3], [2, 3], [11, 5]]}
def test_rating_list():
    m = User(1)
    m.rating_list(user_id_dict)
    assert m.user_rating == [[250, 3], [253, 2], [255, 3], [210, 2], \
                          [12, 3], [10, 5]]
    assert m.user_average == 3

def test_Movie_string():
    m = Movie(1)
    m.movie_title(movie_names_dict)
    m.movie_ratings_and_average(movie_id_dict)
    assert str(m) == "For the movie StarWars the average rating is 3.0."

def test_User_string():
    u = User(1)
    u.rating_list(user_id_dict)
    assert str(u) == "User: 1, has reviewed 6 movies with an average rating of 3.0"

def test_rating_dict():
    u = User(1)
    u.rating_list(user_id_dict)
    u.rating_dict(user_id_dict)
    assert u.user_rating_dict == {250: 3, 253: 2, 255: 3, 210: 2, 12: 3, 10: 5}

def test_movies_reviewed():
    u = User(1)
    u.rating_list(user_id_dict)
    u.movies_reviewed()
    assert u.movies_rated == [250, 253, 255, 210, 12, 10]

def test_compare_user_reviews():
    u = User(1)
    t = User(2)
    u.rating_list(user_id_dict)
    t.rating_list(user_id_dict)
    u.movies_reviewed()
    t.movies_reviewed()
    u.compare_user_reviews(t)
    assert u.common_movies == [250, 253, 10]
    assert u.not_in_common_movies == [55, 2, 11]

def test_make_common_vectors():
    u = User(1)
    t = User(2)
    u.rating_list(user_id_dict)
    t.rating_list(user_id_dict)
    u.rating_dict(user_id_dict)
    t.rating_dict(user_id_dict)
    u.movies_reviewed()
    t.movies_reviewed()
    u.compare_user_reviews(t)
    u.make_common_vectors(t)
    assert u.make_common_vectors(t) == ([3, 2, 5], [1, 1, 3])

v1 = [1, 2, 3, 4, 5, 6]
v2 = [1, 2, 3, 4, 5, 6, 7, 8]
v3 = [1, 2, 3, 4, 5, 6]
v2 = [1, 2, 3, 4, 5, 6]
v4 =

def test_calculate_similarity():
    assert calculate_similarity(v1, v2) = "Vectors are not the same length"
