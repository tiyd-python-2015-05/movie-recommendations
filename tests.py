from movie_data import *
import operator


rates = {(1,60): 3, (1,61): 3, (2,60): 5, (2,61): 2, (4, 67): 3, (3, 67): 3,\
        (3,60): 3, (3,61): 1, (2, 67): 5}

movie = {60: 'ALIEN', 61: 'PROMETHEUS', 67: 'FIGHT CLUB'}


data = Data(movie, rates)


def test_the_rating():
    assert sorted(data.the_rating(60)) == sorted([3,3,5])

def test_avg_rating():
    assert data.avg_rating(61) == (2,3)
    assert data.avg_rating(60) == (4,3)

def test_movie_name():
    assert data.movie_name(67) == 'FIGHT CLUB'

def test_user_ratings():
    assert sorted(data.user_ratings(3)) == sorted([(61,1), (60,3), (67,3)])

def test_top_rated():
    assert sorted(data.top_rated(2, 2)) == sorted([('ALIEN', 4), ('FIGHT CLUB', 4)])

def test_suggested():
    assert sorted(data.suggested(4,2,3)) == sorted([('ALIEN', 4), ('PROMETHEUS', 2)])

def test_similarity():
    assert data.similarity(1,2) == 0.31

def test_recommendations():
    assert data.recommendations(4,0.3) == [(60, 3.0), (61, 3.0)]
