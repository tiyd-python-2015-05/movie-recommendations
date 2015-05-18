from open_file_read import *
from Movie import *
from operator import attrgetter, itemgetter
import os

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
    u_list = make_user_object_list(num_of_users, user_id_dict)
    return [user_id_dict, m_list, u_list, movie_names_dict]

def make_movie_object_list(num_of_movies, movie_id_dict, movie_names_dict):
    """This creates a list of movie objects.
       Each movie includes a movie_title, movie_rating, and average_rating.

       Functional Argument: (num_of_movies, movie_id_dict, movie_names_dict)

           num_of_movies is set to 1682
           movie_id_dict is dict of moive_id: [[user_id, rating], [...], ]
           movie_names_dict is dict of movie_id: movie_title"""

    movies_object_list = []
    for i in range(num_of_movies):
        movies = Movie(i+1)
        movies.movie_title(movie_names_dict)
        movies.movie_ratings_and_average(movie_id_dict)
        movies_object_list.append(movies)
    return movies_object_list

def make_user_object_list(num_of_users, user_id_dict):
    """Creates a list of user objects. Each user includes a
       user_id, user_rating and average_rating

       Functional Arguments: (num_of_users, user_id_dict)

           num_of_users is set to 943
           user_id_dict is dict user_id: [[movie_id, rating], [...], ]"""

    user_object_list = []
    for i in range(num_of_users):
        users = User(i+1)
        users.rating_list(user_id_dict)
        user_object_list.append(users)
    return user_object_list

def movie_sorted_list(m_list, rating_filter=5, length_list=20):
    """Sorts the list of movie objects by the average rating.
       Only movies with 5 or more ratings are included.

    Functional Arguments: (m_list, rating_filter=5, length_list=20)

        m_list = movie objects list
        rating_filter is set to 5
        length_list is set to 20"""

    sort_list = []
    for i in m_list:
        if len(i.movie_rating) >= rating_filter:
            sort_list.append(i)
    sort_list = sorted(sort_list, key=attrgetter("average_rating"), reverse=True)
    # double_sort_list = sorted(sort_list, key=attrgetter("movie_title"))
    top_20 = sort_list[:length_list]
    return top_20

def display_top(m_list):
    sorted_movies = movie_sorted_list(m_list)
    for i in range(len(sorted_movies)):
        print("Movie: {}, Rating: {}".format(sorted_movies[i].movie_title, \
                                        sorted_movies[i].average_rating))
    print("\n")

def user_choice():
    user_answer = input("""What would you like to see?
    1. Top overall movies
    2. Popular movies you haven't seen (requires user id)
    3. Movie recommendations specific to you (requires user id)
    Please enter a number or enter e to exit.\n> """)

    if user_answer == '1':
        return display_top(m_list)

    elif user_answer == '2':
        movies_not_seen = movies_user_not_seen(u_list)
        for i in movies_not_seen:
            print("Movie: {}, Rating: {}".format(i.movie_title, \
                                                 i.average_rating))
        print("\n")

    elif user_answer == '3':
        user_id = int(input("Please enter your user ID#:\n> "))

        sim_users = display_sim_users(u_list, user_id)
        print("Your top three similar users:")
        for i in range(3):
            print("User: {}, Similarity Score: {}"\
                  .format(sim_users[i][0], sim_users[i][1]))
        print("\n")

        movie_recs = display_sim_user_recs(u_list, user_id)
        movie_recs_sim1 = movie_recs[0]
        movie_recs_sim2 = movie_recs[1]
        movie_recs_sim3 = movie_recs[2]
        movie_list_1 = [movie_recs_sim1[i][0] \
                        for i in range(len(movie_recs_sim1))]
        movie_list_2 = [movie_recs_sim2[i][0] \
                for i in range(len(movie_recs_sim2))]
        movie_list_3 = [movie_recs_sim3[i][0] \
                                for i in range(len(movie_recs_sim3))]
        for key in movies_name_dict:
            if key in movie_list_1:
                print("User1 Recommends: {}".format(movies_name_dict[key]))
        print("\n")

        for key in movies_name_dict:
            if key in movie_list_2:
                print("User2 Recommends: {}".format(movies_name_dict[key]))
        print("\n")

        for key in movies_name_dict:
            if key in movie_list_3:
                print("User3 Recommends: {}".format(movies_name_dict[key]))
        print("\n")

    elif user_answer == 'e' or user_choice == 'E':
        return exit()

    else:
        return user_answer()

    second_question = input("Would you like to see anything else? Y/n \n> ")\
                            .upper()
    if second_question == 'Y':
        os.system('clear')
        return user_choice()
    else:
        return exit()

def movies_user_not_seen(u_list, rating_filter=5, length_of_list=20):
    """Displays popular movies the user has not seen.
    The return is the movie objects. To display the Movie and Rating
    you have to call these in the print function in user_answer().

    Functional Arguement: (u_list, rating_filter=5, length_of_list=20)
    u_list = see setup()
    rating_filter = must have 5 or more ratings
    length_of_list = the number of movies returned
    """

    user_id = int(input("Please enter your user ID#:\n> "))
    user = u_list[user_id-1]
    list_of_movies_not_seen = []
    user.movies_reviewed()
    for movie in m_list:
        if len(movie.movie_rating) >= rating_filter:
            if movie.movie_id not in user.movies_rated:
                list_of_movies_not_seen.append(movie)
    list_of_movies_sorted = sorted(list_of_movies_not_seen,\
                                key=attrgetter("average_rating"), reverse=True)
    return list_of_movies_sorted[:length_of_list]

def display_sim_users(u_list, user_id):
    user = u_list[user_id-1]
    user.rating_list(user_id_dict)
    user.rating_dict(user_id_dict)
    user.movies_reviewed()
    for i in u_list:
            i.rating_list(user_id_dict)
            i.rating_dict(user_id_dict)
            i.movies_reviewed()
            user.create_similarity(i)
    top_sim_users = user.top_similar_users()
    return top_sim_users[1:4]

def similar_users(u_list, user_id):
    sim_users = display_sim_users(u_list, user_id)
    sim_user1 = u_list[(sim_users[0][0] - 1)]
    sim_user2 = u_list[(sim_users[1][0] - 1)]
    sim_user3 = u_list[(sim_users[2][0] -1)]
    return [sim_user1, sim_user2, sim_user3]

def display_sim_user_recs(u_list, user_id):
    user = u_list[user_id-1]
    user.rating_list(user_id_dict)
    user.rating_dict(user_id_dict)
    user.movies_reviewed()
    sim_users = similar_users(u_list, user_id)
    sim_user1_top5 = user.movies_not_seen(sim_users[0])
    sim_user2_top5 = user.movies_not_seen(sim_users[1])
    sim_user3_top5 = user.movies_not_seen(sim_users[2])
    movie_rec_id_list = [sim_user1_top5, sim_user2_top5, sim_user3_top5]
    return movie_rec_id_list


if __name__=='__main__':
    start = startup()  #[user_id_dict, m_list, u_list]
    user_id_dict = start[0]
    m_list = start[1]
    u_list = start[2]
    movies_name_dict = start[3]
    user_choice()
    # print(display_sim_user_recs(u_list, 4))
