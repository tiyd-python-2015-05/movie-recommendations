from movie_recommendations import *

'''Using utest.data and utest.item'''

def test_find_all_ratings_for_movie():
    assert sorted(find_all_ratings_for_movie(1)) == [1,2,3,4,5]
    assert sorted(find_all_ratings_for_movie(2)) == [2,2,3,3,4]

def test_average_rating():
    assert average_rating(1) == 3
    assert average_rating(2) == 14/5

def test_get_movie_name():
    assert get_movie_name(2) == 'GoldenEye (1995)'
    assert get_movie_name(4) == 'Get Shorty (1995)'

def test_find_all_ratings_for_user():
    assert sorted(find_all_ratings_for_user(186)) == [1,3]

def test_top_movies():
    assert return_top_movies(5) == ['Secret of Roan Inish, The (1994)',
                                    'Star Trek IV: The Voyage Home (1986)',
                                    'Wizard of Oz, The (1939)',
                                    'Gone with the Wind (1939)',
                                    'Toy Story (1995)']
    assert return_top_movies(3) == ['Secret of Roan Inish, The (1994)',
                                    'Star Trek IV: The Voyage Home (1986)',
                                    'Wizard of Oz, The (1939)']

def test_top_movies_for_user():
    assert top_movies_for_user(118, 5) == ['Secret of Roan Inish, The (1994)',
                                    'Star Trek IV: The Voyage Home (1986)',
                                    'Wizard of Oz, The (1939)',
                                    'Toy Story (1995)','Pink Floyd - The Wall (1982)']

def test_find_common_movies():
    assert common_movies(92,93) == [463]
