from movie_load import *
import csv

item_file = 'u.item'
data_file = 'u.data'
item_list = read_u_item_list(item_file)
data_list = read_u_data_list(data_file)
user_dict = find_all_ratings_of_user(data_list)


    user_login = input(Please enter your 4-digit user number to log in: )
    prompt = input(What kinds of recommendations would you like?
                    1.Top Movies
                    2. Movie recommendations
                    3. Specific user based recommendations

                        Enter 1,2 or 3. )
                    
