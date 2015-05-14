from data_loader import *

"""
943 users
1682 items
100000 ratings
"""

"""
occupations: administrator
artist
doctor
educator
engineer
entertainment
executive
healthcare
homemaker
lawyer
librarian
marketing
none
other
programmer
retired
salesman
scientist
student
technician
writer
"""

def test_data_files_are_present():
    with open("datasets/ml-100k/u.data") as file:
        assert file.readline()
    with open("datasets/ml-100k/u.item") as file:
        assert file.readline()
    with open("datasets/ml-100k/u.user") as file:
        assert file.readline()

def test_num_items():
    ratings = load_data("datasets/ml-100k/u.data")
    assert len(ratings._ratings) == 1682
