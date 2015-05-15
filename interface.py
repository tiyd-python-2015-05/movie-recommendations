from open_file_read import *
from Movie import *

def startup():
    data_file = 'u.data'
    item_file = 'u.item'
    num_of_movies = 1682
    num_of_users = 943
    data_list = movie_data_list(data_file)
    item_list = movie_item_list(item_file)
    user_id_dict = clean_data_to_user_dict(data_list, num_of_users)
    movie_id_dict = clean_data_to_movie_dict(data_list, num_of_movies)
    movie_names_dict = clean_item_to_movie_dict(item_list, num_of_movies)


def make_movie_object_list(num_of_movies, movie_id_dict, movie_names_dict):
    movies_object_list = []
    for i in range(num_of_movies):
        movies = Movie(i+1)
        movies.movie_title(movie_names_dict)
        movies.movie_ratings_and_average(movie_id_dict)
        movies_object_list.append(movies)
    return movies_object_list

def make_user_object_list(num_of_users, user_id_dict):
    user_object_list = []
    for i in range(num_of_users):
        users = User(i+1)
        rating_list(user_id_dict)
        user_object_list.append(users)
    return user_object_list
