from open_file_read import *
from nose.tools import raises

sample_data_list = [['196', '242', '3', '881250949'], ['186', '302', '3', '891717742'], \
['22', '377', '1', '878887116'], ['244', '51', '2', '880606923'], \
['166', '346', '1', '886397596'], ['166', '250', '3', '886397596'], \
['22', '346', '2', '880606923']]

sample_item_list = [['1', 'Toy Story (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)', \
'0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', \
'0', '0', '0', '0', '0', '0', '0'], \
['2', 'GoldenEye (1995)', \
'01-Jan-1995', '', 'http://us.imdb.com/M/title-exact?GoldenEye%20(1995)', \
'0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', \
'0', '1', '0', '0'], \
['3', 'Four Rooms (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Four%20Rooms%20(1995)', '0', '0', '0', '0', \
'0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0'], \
['4', 'Get Shorty (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Get%20Shorty%20(1995)', '0', '1', '0', '0', \
'0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], \
['5', 'Copycat (1995)', '01-Jan-1995', '', \
'http://us.imdb.com/M/title-exact?Copycat%20(1995)', '0', '0', '0', '0', '0', \
'0', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0']]


def test_clean_data_to_user_dict():
    user_dict = clean_data_to_user_dict(sample_data_list, 943)
    assert isinstance(user_dict, dict)
    assert len(sample_data_list) == 7
    # assert user_dict['196'] == ['242', '3']
    # assert 196 == [243,3]

def test_user_dict():
    dictionary = create_dict(5)
    assert len(dictionary) == 5
    assert dictionary[1] == []

def test_data_list_correct_user_dict():
    new_dict = clean_data_to_user_dict(sample_data_list, 943)
    assert new_dict[1] == []
    assert new_dict[196] == [[242, 3]]
    assert new_dict[186] == [[302, 3]]
    assert new_dict[166] == [[346, 1], [250,  3]]

def test_data_list_correct_movie_dict():
    new_dict = clean_data_to_movie_dict(sample_data_list, 1682)
    assert new_dict[1] == []
    assert new_dict[242] == [[196, 3]]
    assert new_dict[302] == [[186, 3]]
    assert new_dict[346] == [[166, 1], [22, 2]]

def test_clean_item_to_movie_dict():
    new_dict = clean_item_to_movie_dict(sample_item_list, 1682)
    assert new_dict[1] == 'Toy Story (1995)'
    assert new_dict[5] == 'Copycat (1995)'
