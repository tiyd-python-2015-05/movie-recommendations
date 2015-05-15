from movie_ratings import dict_read_csv, Movie, Ratings


# def test_read_csv():
#     assert read_csv("sample.csv", "\t") == \
#         [['196', '242', '3', '881250949'],
#          ['186', '302', '3', '891717742'],
#          ['22', '377', '1', '878887116'],
#          ['244', '51', '2', '880606923'],
#          ['166', '346', '1', '886397596']]


def test_dict_read_csv():
    assert dict_read_csv("sample.csv", "\t", "User", "MovieID",
                                       "Rating", "Timestamp") == \
        [{"User": '196', "MovieID": '1',
         "Rating": '3', "Timestamp": '881250949'},
         {"User": '186', "MovieID": '1',
         "Rating": '1', "Timestamp": '891717742'},
         {"User": '22', "MovieID": '2',
         "Rating": '1', "Timestamp": '878887116'},
         {"User": '196', "MovieID": '4',
         "Rating": '2', "Timestamp": '880606923'},
         {"User": '166', "MovieID": '5',
         "Rating": '1', "Timestamp": '886397596'}]


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
    assert movie1.ID == '1'
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


def test_Ratings_makes_dictionary():
    for key in ratings.table:
        if key.title == "Toy Story (1995)":
            assert ratings.table[key] == [["196", "3"], ["186", "1"]]
        elif key.ID == "4":
            assert ratings.table[key] == [["196", "2"]]


def test_Ratings_can_return_movie_ratings():
    assert ratings.get_ratings("1") == ["3", "1"]
    assert ratings.get_ratings("5") == ["1"]


def test_Ratings_can_return_average_movie_rating():
    assert ratings.ratings_avg("1") == "2.0"
    assert ratings.ratings_avg("5") == "1.0"


def test_Ratings_can_return_movie_title():
    assert ratings.movie_title("1") == "Toy Story (1995)"


def test_Ratings_can_return_all_ratings_for_a_user():
    assert ratings.get_user_ratings("196") == [["Get Shorty (1995)", "2"],
                                               ["Toy Story (1995)", "3"]]
    assert ratings.get_user_ratings(196) == [["Get Shorty (1995)", "2"],
                                             ["Toy Story (1995)", "3"]]
