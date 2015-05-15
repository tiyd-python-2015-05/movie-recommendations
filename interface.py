

from file_open_read import *
from classes import *
from operator import attrgetter, itemgetter

#sorted(list_name, key=attrgetter(<attribute>)) "string that is the attribute"
#sort stability

def startup():
    number_users = 943
    number_movies = 1682
    data_file = 'u.data'
    item_file = 'u.item'
    data_list = file_open_read_data_list(data_file)
    item_list = file_open_read_item_list(item_file)
    user_rev_dict = data_list_to_user_dictionary(data_list, number_users)
    movie_rev_dict = data_list_to_movie_dictionary(data_list, number_movies)
    movie_names_dict = item_list_to_movie_names_dictionary(item_list, number_movies)

def make_movie_objects_list(number_movies, movie_names_dict, movie_rev_dict):
    movie_object_list = []
    for i in range(number_movies):
        new_movie = Movie(i + 1)
        new_movie.make_title(movie_names_dict)
        new_movie.make_ratings(movie_rev_dict)
        new_movie.make_movie_average_rating()
        movie_object_list.append(new_movie)
    return movie_object_list


def make_user_objects_list(number_users, user_rev_dict):
    user_object_list = []
    for i in range(number_users):
        new_user = User(i + 1)
        new_user.make_ratings(user_rev_dict)
        user_object_list.append(new_movie)
    return user_object_list
