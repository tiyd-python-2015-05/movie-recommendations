from file_open_read import *
from classes import *
from operator import attrgetter, itemgetter
from numbers import Number

#sorted(list_name, key=attrgetter(<attribute>)) "string that is the attribute"
#sort stability

def startup():
    users = 943
    movies = 1682
    data_file = 'u.data'
    item_file = 'u.item'
    data_list = file_open_read_data_list(data_file)
    item_list = file_open_read_item_list(item_file)
    user_rev_dict = data_list_to_user_dictionary(data_list, users)
    movie_rev_dict = data_list_to_movie_dictionary(data_list, movies)
    movie_names_dict = item_list_to_movie_names_dictionary(item_list, movies)
    m_list = make_movie_objects_list(movies, movie_names_dict, movie_rev_dict)
    u_list = make_user_objects_list(users, user_rev_dict)
    return m_list, u_list

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
        new_user.make_average_rating()
        new_user.make_ratings_dict()
        new_user.movies_reviewed()
        user_object_list.append(new_user)
    return user_object_list


def top_movies(movie_list, length_list=2, min_reviews=1):
    sort_list = []
    for movie in movie_list:
       if len(movie.movie_rating) >= min_reviews:
           sort_list.append(movie)
    sort_list = sorted(sort_list, key=attrgetter('average_rating'), \
               reverse=True)
#   double_sort_list = sorted(sort_list, key=attrgetter('movie_title'))
    top = sort_list[0:length_list]
    return top


def display_top_movies(movie_list, length_list=2, min_reviews=1):
    top = top_movies(movie_list, length_list, min_reviews)
    print("Welcome to the Movie Rating Database.")
    print("Our current top movies are:")
    for i in top:
        print("Movie: {} Average: {}".format(i.movie_title, i.average_rating))


def find_top_movies_not_rated(movie_list, user_list, user_id, \
                              len_list=3, min_rev=1):
    """Makes list of movies not seen by user and sorts them by average rating,
    returns list of desired length."""
    user = user_list[((user_id)-1)]
    user_not_seen_list = []
    for movie in movie_list:
        if movie.movie_id not in user.movies_list:
            if len(movie.movie_rating) >= min_rev:
                user_not_seen_list.append(movie)
    sort_list = sorted(user_not_seen_list, key=attrgetter('average_rating'), \
                   reverse=True)
    top = sort_list[0:len_list]
    return top


def display_top_user_movies(movie_list, user_list, user_id, length_list=2, min_rev=1):
    top = find_top_movies_not_rated(movie_list, user_list, user_id, \
                                    length_list, min_rev)
    for i in top:
        print("Movie: {} Average: {}".format(i.movie_title, i.average_rating))

def choose_user():
    user_id = int(input("What is your user id?:" ))
    if user_id <= 1 or user_id >=944:
        return choose_user()
    else:
        return user_id

def display_user(user_id, u_list):
    print("Welcome User {}".format(user_id))
    u = u_list[(user_id-1)]
    print("You have reviewed {} movies.".format(len(u.rating_list)))
    print("Your average review score is {}".format(u.average_rating))
    print("The top rated movies you have not seen are: ")



def make_user_similarities(user_object):
    """Given current user object, makes a list of tuples with top three
    similar users and their similarity scores."""
    for i in u_list:
        if i.user_id != user_object.user_id:
            user_object.create_similarity_score(i)
    top_similar_users = user_object.create_top_users_in_common()
    return top_similar_users

if __name__ == "__main__":
    while True:
        m_list, u_list = startup()
        display_top_movies(m_list, 20, 5)
        user_id = choose_user()
        u = u_list[(user_id - 1)]
        print(str(u))
        u.movies_reviewed()
        display_user(user_id, u_list)
        display_top_user_movies(m_list, u_list, user_id, length_list=5, min_rev=5)
        similar_users = make_user_similarities(u)
        similar_user_list = i[0] for i in similar_users
        print similar_user_list
        print("Your Top 3 Similar Users are: ")
        for i in similar_users:
            print("User {}, Similarity Score {}".format(i[0], i[1]))

#    for i in top_movies:
#        print("Movie: {} Average: {}".format(i.movie_title, i.average_rating))
###make functions for displaying movie id info in the interface
