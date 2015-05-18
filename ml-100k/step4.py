from movie_load import *
import csv

item_file = 'u.item'
data_file = 'u.data'
item_list = read_u_item_list(item_file)
data_list = read_u_data_list(data_file)
user_dict = find_all_ratings_of_user(data_list)

#Using the return value from step 3, we can run this on all users compared to
#Another. Then compare their similarity rating to the ratings of movies they
#both watched
