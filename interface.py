from open_file_read import *
from Movie import *
from operator import attrgetter, itemgetter


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
    m_list = make_movie_object_list(num_of_movies, \
                                        movie_id_dict, movie_names_dict)
    return m_list

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
        users.rating_list(user_id_dict)
        user_object_list.append(users)
    return user_object_list

def movie_sorted_list(m_list, rating_filter=5, length_list=20):
    sort_list = []
    for i in m_list:
        if len(i.movie_rating) >= rating_filter:
            sort_list.append(i)
    sort_list = sorted(sort_list, key=attrgetter("average_rating"), reverse=True)
    # double_sort_list = sorted(sort_list, key=attrgetter("movie_title"))
    top_20 = sort_list[:length_list]
    return top_20

def display_top():
    m_list = startup()
    sorted_movies = movie_sorted_list(m_list)
    for i in range(len(sorted_movies)):
        print("Movie: {}, Rating: {}".format(sorted_movies[i].movie_title, \
                                        sorted_movies[i].average_rating))

# def display_top_user_none():
#     m_list = startup()
#     sorted_movies = movie_sorted_list(m_list)
#     sorted_user_none = if sorted_movies
#     for i in range(len(sorted_movies)):
#         print("Movie: {}, Rating: {}".format(sorted_movies[i].movie_title, \
#                                         sorted_movies[i].average_rating))

if __name__=='__main__':
    print(display_top())
