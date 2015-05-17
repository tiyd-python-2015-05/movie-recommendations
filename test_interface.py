from file_open_read import *
from nose.tools import raises
from classes import *
from interface import *

number_movies = 3

movie_names_dict = {1: "Star Wars", 2: "Empire Strikes Back",
                    3: "Return of the Jedi"}

movie_ratings_dict = {1: [[345, 2], [545, 5], [645, 3]],
                     2: [[445, 5], [234, 3], [875, 4]],
                     3: [[534, 4], [222, 3], [265, 2]]}

def test_make_movie_objects_list():
    new_movie_list = make_movie_objects_list(number_movies, movie_names_dict,
                                            movie_ratings_dict)
    assert len(new_movie_list) == 3
    assert new_movie_list[0].movie_title == "Star Wars"
    for i in new_movie_list:
        if i.movie_id == 1:
            ratings = i.movie_rating
    assert ratings == [[345, 2], [545, 5], [645, 3]]

number_users = 4

ratings_dict_by_user = {1: [[345, 5], [546, 3], [765, 4]],
                        2: [[42, 4]],
                        3: [[654, 3], [543, 4]],
                        4: [[545, 4], [234, 4], [333, 5], [654, 5], [333, 5]]}


def test_make_user_objects_list():
    new_user_list = make_user_objects_list(number_users, ratings_dict_by_user)
    assert len(new_user_list) == 4
    assert new_user_list[0].user_id == 1
    for i in new_user_list:
        if i.user_id == 1:
            ratings = i.rating_list
    assert ratings == [[345, 5], [546, 3], [765, 4]]

def test_make_top_list():
    new_movie_list = make_movie_objects_list(number_movies, movie_names_dict,
                                                movie_ratings_dict)
    assert len(new_movie_list) == 3
    assert (top_movies(new_movie_list))[0].movie_title == "Empire Strikes Back"
    assert (top_movies(new_movie_list))[1].movie_title == "Star Wars"

def test_display_top_movies_not_rated():
    u = User(1)
    u.movie_list = [1, 2, 3, 4, 5]
    movie1 = Movie(1)
    movie2 = Movie(2)
    movie3 = Movie(3)
    movie4 = Movie(4)
    movie5 = Movie(5)
    movie6 = Movie(6)
    movie7 = Movie(7)
    movie8 = Movie(8)
    movie9 = Movie(9)
    movie10 = Movie(10)
    movie11 = Movie(11)
    movie1.average_rating = 1.2
    movie2.average_rating = 2.2
    movie3.average_rating = 3.2
    movie4.average_rating = 4.2
    movie5.average_rating = 4.5
    movie6.average_rating = 3.2
    movie7.average_rating = 2.2
    movie8.average_rating = 4.2
    movie9.average_rating = 1.2
    movie10.average_rating = 0.2
    movie11.average_rating = 4.7
    movie1.movie_title = "Movie 1"
    movie2.movie_title = "Movie 2"
    movie3.movie_title = "Movie 3"
    movie4.movie_title = "Movie 4"
    movie5.movie_title = "Movie 5"
    movie6.movie_title = "Movie 6"
    movie7.movie_title = "Movie 7"
    movie8.movie_title = "Movie 8"
    movie9.movie_title = "Movie 1"
    movie10.movie_title = "Movie 2"
    movie11.movie_title = "Movie 3"
    movie1.movie_rating = [[1, 4]]
    movie2.movie_rating = [[1, 4]]
    movie3.movie_rating = [[1, 4]]
    movie4.movie_rating = [[1, 4]]
    movie5.movie_rating = [[1, 4]]
    movie6.movie_rating = [[243, 4]]
    movie7.movie_rating = [[243, 4]]
    movie8.movie_rating = [[243, 4]]
    movie9.movie_rating = [[243, 4]]
    movie10.movie_rating = [[243, 4]]
    movie11.movie_rating = [[243, 4]]
    user_list = [u]
    movie_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7,
                    movie8, movie9, movie10, movie11]
    assert find_top_movies_not_rated(movie_list, user_list, 1) == [movie11, movie8, movie6]
