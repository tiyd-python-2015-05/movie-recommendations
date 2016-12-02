from movies import Frame
from driver import Driver

from numbers import Number
from math import sqrt
import nose
import random

data = {(1, 2): 3, (1, 3): 2, (1, 4): 5, (2, 1): 3, (2, 3): 1, (3, 1): 2,
        (3, 2): 1, (3, 3): 5}

names = {2: 'Hello', 3: 'Goodbye', 4: 'What', 1: 'Elephant'}

frame = Frame(names, data)
driver = Driver(frame)

def test_frame_ratings_id():
    assert sorted(frame.ratings_by_id(1)) == sorted([2, 3])

def test_avg_by_id():
    assert frame.average_by_id(1) == (5/2, 2)

def test_movies_by_user():
    assert sorted(frame.movies_by_user(1)) == sorted([2, 3, 4])

def test_name_by_id():
    assert frame.name_by_id(1) == 'Elephant'

def test_top_movies():
    assert frame.top_movies() == []

def test_users():
    assert sorted(frame.users()) == sorted([1,2,3])

def test_e_distance():
    assert driver.e_distance((1,2)) == 1/2
    assert driver.e_distance((2,3)) == driver.e_distance((3,2))
    assert driver.e_distance((2,3)) == 1 / (1 + sqrt(17))

def test_find_e_closest():
    assert sorted(driver.find_closest(2, driver.e_distance)) == sorted([(1,1/2),
                                                       (3,1/(1+sqrt(17)))])

def test_find_e_rec():
    print(driver.find_rec(2, driver.e_distance))
    assert sorted(driver.find_rec(2, driver.e_distance)) == sorted(['Hello', 'What'])

def test_p_disance():
    assert isinstance(driver.p_distance([1, 2]), Number)
    assert -1 <= driver.p_distance([1, 2]) <= 1
    assert driver.p_distance([1, 2]) == driver.p_distance([2, 1])


if __name__ == '__main__':
    nose.main()
