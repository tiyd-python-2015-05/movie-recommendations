from movies import *


movie1 = Movie(1, "", 1, 1, "")
movie1.add_rating(1, 3)
movie1.add_rating(2, 5)

movie2 = Movie(2, "", 1, 1, "")
movie2.add_rating(2, 3)
movie2.add_rating(3, 4)

m_dict = {1: movie1,
          2: movie2}


def test_avg():
    assert movie1.avg() == 4


def test_add():
    print(movie1 + movie2)
    assert ([2], [5], [3]) == movie1 + movie2


def test_similar():
    ids, scs = movie1.similar(m_dict)
    print(ids)
    assert ids == [0, 0, 0, 0, 0]
