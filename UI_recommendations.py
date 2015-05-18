from operator import itemgetter
import movie_ratings
import recommendations
import os


user_ratings = movie_ratings.dict_read_csv("ml-100k/u.data", "\t", "User",
                                           "MovieID", "Rating", "Timestamp")
movies = movie_ratings.dict_read_csv("ml-100k/u.item", "|",
                                     'MovieID', 'Movie Title', 'release date',
                                     'video release date', 'IMDb URL',
                                     'unknown', 'Action', 'Adventure',
                                     'Animation', "Children's", 'Comedy',
                                     'Crime', 'Documentary', 'Drama',
                                     'Fantasy', 'Film-Noir', 'Horror',
                                     'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                                     'Thriller', 'War', 'Western')

ratings = movie_ratings.Ratings(movies, user_ratings)

recommender = recommendations.Recommender(ratings)


def menu():
    # os.system('clear')
    print("Welcome to the MovieMatrix movie rating and recommendation system.")
    print("(Powered by MovieLens database)")
    print("Please enter the number of the menu item you wish to access")
    print("1) Look-up movie titles and IDs")
    print("2) See rating distribution for a movie by ID")
    print("3) See top movies")
    print("4) See top movies for user by average movie rating")
    print("5) See top movies for user by pearson correlation")
    print("6) See top movies for user by euclidean distance")
    print("7) Create new user")
    print("8) Rate a movie")
    print("0) Quit")
    try:
        navigation = int(input(
            "Please enter the number of the option you wish to access: "))
    except:
        os.system('clear')
        print("Invalid choice! Please try again.")
        return menu()

    if navigation in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        if navigation == 1:
            os.system('clear')
            return movie_list()
        elif navigation == 2:
            os.system('clear')
            return movie_ratings()
        elif navigation == 3:
            os.system('clear')
            return top_movies()
        elif navigation == 4:
            os.system('clear')
            return top_user_movies()
        elif navigation == 5:
            os.system('clear')
            return pearson_recommendation()
        elif navigation == 6:
            os.system('clear')
            return euclidean_recommendation()
        elif navigation == 7:
            os.system('clear')
            return add_new_user()
        elif navigation == 8:
            os.system('clear')
            return add_new_rating()
        elif navigation == 0:
            print("Thank you for using MovieMatrix.  I hope it worked.")
            return
    else:
        os.system('clear')
        print("Invalid choice! Please try again.")
        return menu()


def movie_list():
    print("Here you can find listings of all movies rated.")
    print("They are sorted alphabetically, so please enter the first letter")
    print("of the movie you would like to look up.  If the movie title")
    print("begins with an article, use the letter of the following word.")
    print("If it begins with a number, enter 1.")
    navigation = input("Please enter your choice: ").lower()

    if navigation in "abcdefghijklmnopqrstuvwxyz1":
        return movie_list2(navigation)
    else:
        os.system('clear')
        print("Invalid choice! Please try again.")
        return movie_list()


def movie_list2(character):
    if character == "1":
        return alpha_sort("1234567890")
    else:
        return alpha_sort(character)


def alpha_sort(character):
    movie_list = []
    for movie in ratings.movie_table:
        if movie.title[0].lower() in character:
            movie_list.append(
                ((str(movie.ID)), movie.title))
    for movie in sorted(movie_list, key=itemgetter(1)):
        print(movie[0].ljust(5) + "| " + movie[1])

    return back_to_menu()


def movie_ratings():
    movie = int(
        input(
            "Please enter the numerical ID \
of the movie whose ratings you wish to see. "))

    movie_ratings = sorted(ratings.get_ratings(movie), reverse=True)
    freq = {}
    for number in movie_ratings:
        freq[number] = freq.get(number, 0) + 1

    for key in freq:
        print(str(key).ljust(2) + "| " +
              ("#"*((int(freq[key]))//(int(max(freq.values())/10)))).rjust(1))

    return back_to_menu()


def top_movies():
    number = int(input("How many top movies would you like to see? "))
    movies = recommender.topx(cut_off=number)
    for movie in movies:
        print(str(movie[1]).ljust(5) + "| " + movie[0])

    return back_to_menu()


def top_user_movies():
    user = int(input("What is the numerical ID of the user(1-{})? ".format(
        str(len(ratings.user_table)))))
    number = int(input("How many top movies would you like to see? "))
    movies = recommender.topx_for_user(user, cut_off=number)
    for movie in movies:
        print(str(movie[1]).ljust(5) + "| " + movie[0])

    return back_to_menu()


def pearson_recommendation():
    user = int(input(
        "What is the numerical ID of the user(1-{})? ".format(
            str(len(ratings.user_table)))))
    number = int(input("How many top movies would you like to see? "))
    movies = recommender.user_recommendation(user, cut_off=number)
    for movie in movies:
        print(movie)

    return back_to_menu()


def euclidean_recommendation():
    user = int(input("What is the numerical ID of the user(1-{})? ".format(
        str(len(ratings.user_table)))))
    number = int(input("How many top movies would you like to see? "))
    movies = recommender.user_recommendation(
        user, cut_off=number, pearson=False)
    for movie in movies:
        print(movie)

    return back_to_menu()


def add_new_user():
    userID = (len(ratings.user_table) + 1)
    ratings.user_table[userID] = []
    print("Your user ID is {}".format(str(userID)))

    return back_to_menu()


def add_new_rating():
    userID = int(input("What is your userID? "))
    if userID in ratings.user_table:
        movieID = int(
            input("What is the numerical ID of the movie you wish to rate? "))
        rating = int(
            input("What rating (1-5, 5 high) would you like to give it? "))

        ratings.user_table[userID].append([movieID, rating])
    else:
        print("That is not a valid userID")

        navigation = input(
            "Would you like to rate another movie (y/n)? ").lower()

    if navigation[0] in "yn":
        if navigation[0] == "y":
            return add_new_rating()
        else:
            return back_to_menu()
    else:
        print("Invalid choice! Please try again.")
        return back_to_menu()


def back_to_menu():
    navigation = input(
        "Would you like to return to the main menu (y/n)? ").lower()

    if navigation[0] in "yn":
        if navigation[0] == "y":
            os.system('clear')
            return menu()
        else:
            print("Thank you for using MovieMatrix.  I hope it worked.")
            return
    else:
        print("Invalid choice! Please try again.")
        return back_to_menu()

if __name__ == '__main__':
    menu()
