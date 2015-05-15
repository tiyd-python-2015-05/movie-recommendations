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

user_id_dict = {196:[[250, 3], [253, 2], [255, 3], [210, 2], [12, 3], [10, 5]]}

def test_review_list():
    m = User(196)
    m.rating_list(user_id_dict)
    assert m.user_rating == [[250, 3], [253, 2], [255, 3], [210, 2], \
                          [12, 3], [10, 5]]
