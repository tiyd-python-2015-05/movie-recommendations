from operator import attrgetter, itemgetter
import csv


def file_open_read_data_list(data_file):
    """For opening the u.data file to a list of lists"""
    with open(data_file, encoding='windows-1252') as file:
        reader = csv.reader(file, delimiter='\t')
        data_list = [i for i in reader]
    return data_list


def file_open_read_item_list(item_file):
    """For opening the u.item file to a list of lists."""
    with open(item_file, encoding='windows-1252') as file:
        reader = csv.reader(file, delimiter="|")
        data_list = [i for i in reader]
    return data_list


def create_dictionary(length):
    """creates a new dictionary of chosen length with keys in range(length)
    and initial value of empty list"""
    new_dict = {}
    for i in range(length):
        new_dict[i+1] = []
    return new_dict


def create_dictionary_string(length):
    """creates a new dictionary of chosen length with keys in range(length)
    and initial value of empty string"""
    new_dict = {}
    for i in range(length):
        new_dict[i+1] = ""
    return new_dict


def data_list_to_user_dictionary(data_list, number_users):
    """Creates a new dictionary of given length and appends data from
    data set.  The key will be the user id, the values a list of lists.
    Each list is a movie id and a rating"""
    user_dict = create_dictionary(number_users)
    for a in data_list:
        user_dict[int(a[0])].append([int(a[1]), int(a[2])])
    return user_dict


def data_list_to_movie_dictionary(data_list, number_movies):
    """Creates a new dictionary of given length and appends data from
    data set.  The key will be the movie id, the values a list of lists.
    Each list is a user id and a rating"""
    movie_dict = create_dictionary(number_movies)
    for a in data_list:
        movie_dict[int(a[1])].append([int(a[0]), int(a[2])])
    return movie_dict


def item_list_to_movie_names_dictionary(item_list, number_movies):
    """Creates a new dictionary of given length and appends data from
    data set.  The key will be the movie id, the values a list of lists.
    Each list is a user id and a rating"""
    movie_names_dict = create_dictionary_string(number_movies)
    for a in item_list:
        movie_names_dict[int(a[0])] = (a[1])
    return movie_names_dict





if __name__ == "__main__":
    number_users = 943
    number_movies = 1682
    data_file = 'u.data'
    item_file = 'u.item'
    data_list = file_open_read_data_list(data_file)
    item_list = file_open_read_item_list(item_file)
    user_rev_dict = data_list_to_user_dictionary(data_list, number_users)
    movie_rev_dict = data_list_to_movie_dictionary(data_list, number_movies)
    movie_names_dict = item_list_to_movie_names_dictionary(item_list, number_movies)
    # print(movie_names_dict[67])
    # print(movie_names_dict[1500])
    # print(movie_rev_dict[500])
    # print(movie_rev_dict[650])
    # print(user_rev_dict[450])
    # print(user_rev_dict[35])
