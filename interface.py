from file_open_read import *
from classes import *

def Startup():
    number_users = 943
    number_movies = 1682
    data_file = 'u.data'
    item_file = 'u.item'
    data_list = file_open_read_data_list(data_file)
    item_list = file_open_read_item_list(item_file)
    user_rev_dict = data_list_to_user_dictionary(data_list, number_users)
    movie_rev_dict = data_list_to_movie_dictionary(data_list, number_movies)
    movie_names_dict = item_list_to_movie_names_dictionary(item_list, number_movies)
