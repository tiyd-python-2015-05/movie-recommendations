import csv

def movie_data_dict(data_file):
    with open(data_file, encoding='windows-1252') as file:
        reader = csv.DictReader(file, delimiter='\t', \
                 fieldnames=("user id", "movie id", "rating", "timestamp"))
        open_movie_data_dict = [row for row in reader]
        return open_movie_data_dict

def movie_item_dict(item_file):
    with open(item_file, encoding='windows-1252') as file:
        reader = csv.DictReader(file, delimiter='|', \
                 fieldnames=("movie id", "movie title", "release date", \
                 "video release date", "IMDb URL", "unknown", "Action", \
                 "Adventure", "Animation", "Children's", "Comedy", \
                 "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", \
                 "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", \
                 "Thriller", "War", "Western"))
        open_movie_item_dict = [row for row in reader]
        return open_movie_item_dict

"""Could not decide which version of dictionary to use. The functions above
create dictionaries with values as dictionaries"""

def movie_data_list(data_file):
    with open(data_file, encoding='windows-1252') as file:
        reader = csv.reader(file, delimiter='\t')
        open_movie_data_list = [row for row in reader]
        return open_movie_data_list

def movie_item_list(item_file):
    with open(item_file, encoding='windows-1252') as file:
        reader = csv.reader(file, delimiter='|')
        open_movie_item_list = [row for row in reader]
        return open_movie_item_list

def create_dict(length):
    """Creates dictionary with user id as the key and an empty list
    as the value. the function clean_data_to_user_dict(data_list, num_of_users)
    appends the movie ids and ratings to the user id keys.
    Functional Arguments:length"""

    new_dict = {}
    for i in range(length):
        new_dict[i+1] = []
    return new_dict

def create_dict_str(length):
    """Creates dictionary with user id as the key and an empty list
    as the value. the function clean_data_to_user_dict(data_list, num_of_users)
    appends the movie ids and ratings to the user id keys.
    Functional Arguments:length"""

    new_dict = {}
    for i in range(length):
        new_dict[i+1] = ""
    return new_dict

def clean_data_to_user_dict(data_list, num_of_users):
    """Creates user dictionary with userid as the key.
    The values are movie id and rating.

    Functional Arguments:
    (data_list, num_of_users)"""

    user_dict = create_dict(num_of_users)
    for a in data_list:
        user_dict[int(a[0])].append([int(a[1]), int(a[2])])
    return user_dict
    # for i in range(len(data_list))
    # user_dict.setdefault(data_list[i][i], d)

def clean_data_to_movie_dict(data_list, num_of_movies):
    """Creates movie dictionary with movie id as the key.
    The values are user id and rating.

    Functional Arguments:
    (data_list, num_of_movies)"""

    movie_dict = create_dict(num_of_movies)
    for a in data_list:
        movie_dict[int(a[1])].append([int(a[0]), int(a[2])])
    return movie_dict

def clean_item_to_movie_dict(item_list, num_of_movies):
    """Creates a dictionary with movie id as the key and value as the title.

    Functional Arguments:
    (item_list, num_of_movies)"""
    movies_dict_title = create_dict_str(num_of_movies)
    for a in item_list:
        movies_dict_title[int(a[0])] = a[1]
    return movies_dict_title
        # movies_dict_title = {}
        # movies_dict_title.setdefault(int(a[0]), a[1])

if __name__=='__main__':
    pass
    # data_file = 'u.data'
    # item_file = 'u.item'
    # num_of_movies = 1682
    # num_of_users = 943
    # data_list = movie_data_list(data_file)
    # item_list = movie_item_list(item_file)
    # user_id_dict = clean_data_to_user_dict(data_list, num_of_users)
    # movie_id_dict = clean_data_to_movie_dict(data_list, num_of_movies)
    # movie_names_dict = clean_item_to_movie_dict(item_list, num_of_movies)
