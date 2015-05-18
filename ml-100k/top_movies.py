from movie_load import *
import csv

def top_movies(average_dict):
    number = input("What number of top movies would you like to see? ")

    sorted_dict = sorted(average_dict.items(), key=lambda x: x[1], reverse=True)

    for i in range(int(number)):
        print (sorted_dict[i])








if __name__=='__main__':
    item_file = 'u.item'
    data_file = 'u.data'
    item_list = read_u_item_list(item_file)
    data_list = read_u_data_list(data_file)
    rating_dict = find_ratings_by_ID(data_list)
    average_dict = find_average_rating_of_movie_by_ID(rating_dict)
    top_movies(average_dict)
    # print(find_all_ratings_of_user(data_list))
