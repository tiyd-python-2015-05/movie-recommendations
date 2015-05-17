from movie_ratings import dict_read_csv, Movie, Ratings


# def test_read_csv():
#     assert read_csv("sample.csv", "\t") == \
#         [[196, 1, 3],
#          [186, 1, 2],
#          [22, 2, 1],
#          [196, 4, 2],
#          [166, 5, 1],
#          [166, 3, 4]
#          [186, 4, 3]]


def test_dict_read_csv():
    assert dict_read_csv("sample.csv", "\t", "User", "MovieID",
                                       "Rating", "Timestamp") == \
        [{"User": 196, "MovieID": 1,
         "Rating": 3},
         {"User": 186, "MovieID": 1,
         "Rating": 2},
         {"User": 22, "MovieID": 2,
         "Rating": 1},
         {"User": 196, "MovieID": 4,
         "Rating": 2},
         {"User": 166, "MovieID": 5,
         "Rating": 1},
         {"User": 166, "MovieID": 3,
         "Rating": 4},
         {"User": 186, "MovieID": 4,
         "Rating": 3},
         {"User": 186, "MovieID": 6,
         "Rating": 5}]


def test_Movie_has_params():
    movie_list = dict_read_csv("sample2.csv", "|",
                               'MovieID', 'Movie Title', 'release date',
                               'video release date', 'IMDb URL', 'unknown',
                               'Action', 'Adventure', 'Animation',
                               "Children's", 'Comedy', 'Crime', 'Documentary',
                               'Drama', 'Fantasy', 'Film-Noir', 'Horror',
                               'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                               'Thriller', 'War', 'Western')
    movie1 = Movie(movie_list[0])
    assert movie1.ID == 1
    assert movie1.title == "Toy Story (1995)"
    assert movie1.genre == {'Animation', "Children's", 'Comedy'}


user_ratings = dict_read_csv("sample.csv", "\t", "User", "MovieID",
                             "Rating", "Timestamp")
movies = dict_read_csv("sample2.csv", "|",
                       'MovieID', 'Movie Title', 'release date',
                       'video release date', 'IMDb URL', 'unknown',
                       'Action', 'Adventure', 'Animation',
                       "Children's", 'Comedy', 'Crime', 'Documentary',
                       'Drama', 'Fantasy', 'Film-Noir', 'Horror',
                       'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                       'Thriller', 'War', 'Western')

ratings = Ratings(movies, user_ratings)


def test_Ratings_makes_movie_dictionary():
    for key in ratings.movie_table:
        if key.title == "Toy Story (1995)":
            assert sorted(ratings.movie_table[key]) == sorted([[196, 3], [186, 2]])
        elif key.ID == 4:
            assert sorted(ratings.movie_table[key]) == sorted([[196, 2], [186, 3]])


def test_Ratings_can_return_movie_ratings():
    assert sorted(ratings.get_ratings(1)) == sorted([3, 2])
    assert sorted(ratings.get_ratings(5)) == sorted([1])


def test_Ratings_can_return_average_movie_rating():
    assert ratings.ratings_avg(1) == 2.5
    assert ratings.ratings_avg(5) == 1.0


def test_Ratings_can_return_movie_title():
    assert ratings.movie_title(1) == "Toy Story (1995)"


def test_Ratings_can_return_all_ratings_for_a_user():
    assert ratings.get_user_ratings(196) == [["Get Shorty (1995)", 2],
                                             ["Toy Story (1995)", 3]]
