from movie_load import *
import csv

item_file = 'u.item'
data_file = 'u.data'
item_list = read_u_item_list(item_file)
data_list = read_u_data_list(data_file)
user_dict = find_all_ratings_of_user(data_list)


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    item_file = 'u.item'
    data_file = 'u.data'
    item_list = read_u_item_list(item_file)
    data_list = read_u_data_list(data_file)
    user_dict = find_all_ratings_of_user(data_list)

    # Need help getting this specific list from the dictionary set-up I have
    def similar(self, other, user_dict):
        for


    def euclidean_distance(v, w):
        """Given two lists, give the Euclidean distance between them on a scale
        of 0 to 1. 1 means the two lists are identical.
        """

        # Guard against empty lists.
        if len(v) is 0:
            return 0

        # Note that this is the same as vector subtraction.
        differences = [v[idx] - w[idx] for idx in range(len(v))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)

        return 1 / (1 + math.sqrt(sum_of_squares))
