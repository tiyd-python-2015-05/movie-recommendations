from file_open_read import *
from classes import *
from operator import attrgetter, itemgetter
from numbers import Number


def startup():
    """Gets data from u.data and u.list and stores user and movie objects in
    two separate lists."""
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
    """Makes movie objects list for startup."""
    movie_object_list = []
    for i in range(number_movies):
        new_movie = Movie(i + 1)
        new_movie.make_title(movie_names_dict)
        new_movie.make_ratings(movie_rev_dict)
        new_movie.make_movie_average_rating()
        movie_object_list.append(new_movie)
    return movie_object_list


def make_user_objects_list(number_users, user_rev_dict):
    """Makes user object list for startup."""
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
    """Makes top movie list for initial display with min number
    of reviews filter."""
    sort_list = []
    for movie in movie_list:
       if len(movie.movie_rating) >= min_reviews:
           sort_list.append(movie)
    sort_list = sorted(sort_list, key=attrgetter('average_rating'), \
               reverse=True)
    top = sort_list[0:length_list]
    return top


def display_top_movies(movie_list, length_list=2, min_reviews=1):
    """Displays top movie list in interface."""
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
    """Displays the top movies user hasn't seen in interface."""
    top = find_top_movies_not_rated(movie_list, user_list, user_id, \
                                    length_list, min_rev)
    print("The top rated movies you have not seen are: ")
    for i in top:
        print("Movie: {} Average: {}".format(i.movie_title, i.average_rating))


def choose_user():
    """Asks user for id to access user info."""
    try:
        user_id = int(input("What is your User ID?: "))
        if user_id not in range(1,944):
            return choose_user()
        else:
            return (user_id)
    except ValueError:
        print("Numbers only!!")
        return choose_user()


def display_user(user_id, u_list):
    """Displays user info after login."""
    print("Welcome User {}".format(user_id))
    u = u_list[(user_id-1)]
    print("You have reviewed {} movies.".format(len(u.rating_list)))
    print("Your average review score is {}".format(u.average_rating))


def make_user_similarities(user_object):
    """Given current user object, makes a list of tuples with top three
    similar users and their similarity scores."""
    for i in u_list:
        if i.user_id != user_object.user_id:
            user_object.create_similarity_score(i)
    top_similar_users = user_object.create_top_users_in_common()
    return top_similar_users


def user_options():
    """Displays user options after login."""
    print("What would you like to do?")
    print("1. See the top rated movies you haven't seen.")
    print("2. See a list of similar users with recommendations.")
    user_input= int(input("Choose 1 or 2: "))
    if user_input > 2 or user_input < 1:
        return user_option()
    else:
        return user_input


def display_sim_user_recs(similar_users, u_list):
    """Displays recommendations from most similar users in interface."""
    similar_user_list = [i[0] for i in similar_users]
    sim_user1 = u_list[(similar_user_list[0]-1)]
    sim_user2 = u_list[(similar_user_list[1]-1)]
    sim_user3 = u_list[(similar_user_list[2]-1)]
    top_rec_sim_user1 = u.movies_reviewed_not_seen(sim_user1)
    top_rec_sim_user2 = u.movies_reviewed_not_seen(sim_user2)
    top_rec_sim_user3 = u.movies_reviewed_not_seen(sim_user3)
    print("For User {}, your top recommmendations are: ".format(sim_user1.user_id))
    for i in top_rec_sim_user1:
        movie_id = i[0]
        rating = i[1]
        movie = m_list[(movie_id) - 1]
        print("{}, Rated {}".format(movie.movie_title, rating))
    print("For User {}, your top recommmendations are: ".format(sim_user2.user_id))
    for i in top_rec_sim_user2:
        movie_id = i[0]
        rating = i[1]
        movie = m_list[movie_id - 1]
        print("{}, Rated {}".format(movie.movie_title, rating))
    print("For User {}, your top recommmendations are: ".format(sim_user3.user_id))
    for i in top_rec_sim_user3:
        movie_id = i[0]
        rating = i[1]
        movie = m_list[movie_id - 1]
        print("{}, Rated {}".format(movie.movie_title, rating))


def user_quit():
    quit = (input("Would you like to quit? (Y/n): ")).lower()
    if quit == "n":
        return False
    else:
        return True


# def user_interface():
#     while True:
#         m_list, u_list = startup()
#         display_top_movies(m_list, 20, 5)
#         user_id = choose_user()
#         u = u_list[(user_id - 1)]
#         u.movies_reviewed()
#         display_user(user_id, u_list)
#         user_choice = user_options()
#         if user_choice == 1:
#             display_top_user_movies(m_list, u_list, user_id,
#                                     length_list=5, min_rev=5)
#         if user_choice == 2:
#             similar_users = make_user_similarities(u)
#             display_sim_user_recs(similar_users, u_list)
#         if user_quit():
#             break


if __name__ == "__main__":
#    user_interface()
    while True:
        m_list, u_list = startup()
        display_top_movies(m_list, 10, 5)
        user_id = choose_user()
        u = u_list[(user_id - 1)]
        u.movies_reviewed()
        display_user(user_id, u_list)
        user_choice = user_options()
        if user_choice == 1:
            display_top_user_movies(m_list, u_list, user_id,
                                    length_list=20, min_rev=5)
        if user_choice == 2:
            similar_users = make_user_similarities(u)
            display_sim_user_recs(similar_users, u_list)
        if user_quit():
            break
