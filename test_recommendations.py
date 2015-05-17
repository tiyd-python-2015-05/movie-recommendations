from movie_ratings import dict_read_csv, Movie, Ratings
import recommendations2


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

recommender = recommendations2.Recommender(ratings)

recommender_2 = recommendations2.Recommender(ratings, movie_filter=1)

recommender_3 = recommendations2.Recommender(ratings, user_filter=2, movie_filter=2)


def test_movie_avgs():
    assert sorted(recommender.movie_avgs) == \
        [[1, 2.5], [2, 1.0], [3, 4.0], [4, 2.5], [5, 1.0], [6, 5.0]]


def test_top_returns_correct_order():
    assert recommender_2.top == \
        [["Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)", 5.0],
         ["Four Rooms (1995)", 4.0], ["Get Shorty (1995)", 2.5],
         ["Toy Story (1995)", 2.5], ["Copycat (1995)", 1.0],
         ["GoldenEye (1995)", 1.0]]


def test_top_limits_by_number_of_ratings():
    assert recommender_3.top == \
        [["Get Shorty (1995)", 2.5], ["Toy Story (1995)", 2.5]]


def test_topx_limits_number_of_top_movies():
    assert recommender_2.topx(cut_off=4) == \
        [["Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)", 5.0],
         ["Four Rooms (1995)", 4.0], ["Get Shorty (1995)", 2.5],
         ["Toy Story (1995)", 2.5]]


def test_bottomx_limits_number_of_bottom_movies():
    assert recommender_2.bottomx(cut_off=4) == \
        [["Get Shorty (1995)", 2.5],
         ["Toy Story (1995)", 2.5], ["Copycat (1995)", 1.0],
         ["GoldenEye (1995)", 1.0]]


def test_topx_for_user():
    assert recommender_2.topx_for_user(196, cut_off=4) == \
        [["Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)", 5.0],
         ["Four Rooms (1995)", 4.0],
         ["Copycat (1995)", 1.0],
         ["GoldenEye (1995)", 1.0]]

test_user1 = [196, [[1, 3], [4, 2]]]
test_user2 = [186, [[1, 2], [4, 3]]]
test_user3 = [19, [[1, 3], [2, 4], [3, 4], [4, 2]]]
test_user4 = [16, [[1, 2], [2, 3], [3, 3], [4, 1], [5, 2], [6, 3]]]
test_user5 = [18, [[1, 3], [2, 5], [3, 3], [4, 2], [5, 3], [6, 2]]]
test_user6 = [12, [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]]
users_list = [test_user3, test_user4, test_user5, test_user6]

def test_user_match():
    assert recommender.user_match(test_user1[1], test_user2[1]) == \
        [(3, 2),
         (2, 3)]


user_ratings2 = dict_read_csv("sample3.csv", "\t", "User", "MovieID",
                             "Rating", "Timestamp")

movies2 = dict_read_csv("sample2.csv", "|",
                       'MovieID', 'Movie Title', 'release date',
                       'video release date', 'IMDb URL', 'unknown',
                       'Action', 'Adventure', 'Animation',
                       "Children's", 'Comedy', 'Crime', 'Documentary',
                       'Drama', 'Fantasy', 'Film-Noir', 'Horror',
                       'Musical', 'Mystery', 'Romance', 'Sci-Fi',
                       'Thriller', 'War', 'Western')

ratings2 = Ratings(movies2, user_ratings2)

recommender2 = recommendations2.Recommender(ratings2)


def test_pearson_score():
    assert round(recommender_3.pearson_score(test_user1[1], test_user2[1]), 2) == -1
    assert round(recommender2.pearson_score(test_user3[1], test_user4[1]), 2) == 1.0


def test_euclidean_distance():
    assert round(recommender_3.euclidean_distance(
        test_user1[1], test_user2[1]), 2) == 0.41


def test_similarity_score():
    assert recommender2.similarity_score(test_user3, [test_user4], recommender2.pearson_score) == \
        [['Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)', 3.0],
         ['Copycat (1995)', 2.0]]


def test_user_recommendation():
    assert recommender2.user_recommendation(19) == \
    ["Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)",
     "Copycat (1995)"]
    assert recommender2.user_recommendation(19, pearson=False) == \
    ["Copycat (1995)",
     "Shanghai Triad (Yao a yao yao dao waipo qiao) (1995)"]
