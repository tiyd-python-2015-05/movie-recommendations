from interface import *
from nose.tools import raises
from operator import attrgetter, itemgetter


movie_names_dict = {1: "StarWars", 2: "Pig", 3: "ToyStory", 4: "RainMan"}
movie_id_dict = {1:[[25, 3], [253, 2], [255, 3], [210, 2], [12, 3], [10, 5]],\
                2:[[52, 4], [325, 4], [552, 4], [102, 4], [21, 4], [1, 4]]}
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

def test_movie_sorted_list():
    new_movie_list = make_movie_object_list(num_of_movies, movie_id_dict, movie_names_dict)
    assert movie_sorted_list(new_movie_list)[0] == new_movie_list[1]

# user = User(10)
# user.movies_rated = [i for i in range(1:20)]
# movie_list_w_avg_rating = generator()

# def generator():
#     ratings = [[1, 1], [1, 2], [1, 2, 3, 4, 5], [1, 2, 3]]
#     gen_movie_rating_dict = {}
#     for i in range(1,41):
#         for x in ratings:
#             gen_movie_rating_dict(i, x)
#     return gen_movie_rating_dict
#
# def test_movies_user_not_seen(user_id):
#     user = User(10)
#     movie.movie_rating = generator()
#     u_list = [i for i in range(1,15)]
#     user = 10
#     user.movies_rated = [i for i in range(1,15)]
#     movie.movie_rating =
#     assert movies_user_not_seen(u_list, rating_filter=3, length_of_list=5) ==\


    list_of_movies_not_seen = []
    for movie in m_list:
        if movie.movie_id not in user.movies_rated:
            list_of_movies_not_seen.append(movie.movie_id)
            return sorted(list_of_movies_not_seen)
