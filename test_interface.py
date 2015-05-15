from interface import *
from nose.tools import raises
from operator import attrgetter, itemgetter

#sorted(list_name, key=attrgetter(<attribute>))"""Put in string that is attribute"""



movie_names_dict = {1: "StarWars", 2: "Pig", 3: "ToyStory", 4: "RainMan"}
movie_id_dict = {1:[[25, 3], [253, 2], [255, 3], [210, 2], [12, 3], [10, 5]],\
                2:[[52, 2], [325, 1], [552, 3], [102, 1], [21, 4], [1, 4]]}
user_id_dict = {1:[[250, 3], [253, 2], [255, 3], [210, 2], [12, 3], [10, 5]],\
                2:[[50, 1], [53, 1], [55, 4], [10, 3], [2, 3], [11, 5]]}
num_of_movies = 2
num_of_users = 2

def test_make_movie_object_list():
    new_movie_list = make_movie_object_list(num_of_movies, movie_id_dict, movie_names_dict)
    assert new_movie_list[0].movie_title == "StarWars"
    assert len(new_movie_list) == 2
    for i in new_movie_list:
        if i.movie_id == 1:
            ar = i.average_rating
    assert ar == 3

def test_make_user_object_list():
    new_user_list = make_user_object_list(num_of_users, user_id_dict)
    assert new_user_list[0].user_rating == [[250, 3], [253, 2], [255, 3],\
                                            [210, 2], [12, 3], [10, 5]]
