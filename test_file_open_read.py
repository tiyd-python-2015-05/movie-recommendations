from file_open_read import *
from nose.tools import raises
from classes import *

data_list = [['196', '242', '3', '881250949'],
['186', '302', '3', '891717742'],
['22', '377', '1', '878887116'],
['244', '51', '2', '880606923'],
['166', '346', '1', '886397596'],
['166', '245', '5', '878658493'],
['24', '245', '5', '834569349']]

item_list = [['1', 'Toy Story (1995)', '01-Jan-1995', '', \
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



def test_data_list_to_user_dict():
    user_dict = data_list_to_user_dictionary(data_list, 943)
    assert isinstance (user_dict, dict)
    assert len(user_dict) == 943
#    assert user_dict['196'] == [['242', '3']]

def test_create_dict():
    new = create_dictionary(5)
    assert len(new)  == 5
    assert new[1] == []
    assert new[5] == []

def test_create_dict_string():
    new = create_dictionary_string(1682)
    assert len(new)  == 1682
    assert new[1] == ""
    assert new[5] == ""
    assert new[9] == ""
    assert new[1682] == ""

def test_data_list_creates_correct_user_dict():
    new_dict = data_list_to_user_dictionary(data_list, 943)
    assert new_dict[1] == []
    assert new_dict[943] == []
    assert new_dict[196] == [[242, 3]]
    assert new_dict[186] == [[302, 3]]
    assert new_dict[166] == [[346, 1], [245, 5]]

def test_data_list_creates_correct_movie_dict():
    new_dict = data_list_to_movie_dictionary(data_list, 1682)
    assert new_dict[1] == []
    assert new_dict[1682] == []
    assert new_dict[242] == [[196, 3]]
    assert new_dict[302] == [[186, 3]]
    assert new_dict[245] == [[166, 5], [24, 5]]

def test_item_list_creates_correct_movie_names_dict():
    new_dict = item_list_to_movie_names_dictionary(item_list, 1682)
    assert new_dict[1] == 'Toy Story (1995)'
    assert new_dict[2] == 'GoldenEye (1995)'
    assert new_dict[5] == 'Copycat (1995)'
    assert new_dict[1682] == ""

def test_clean_item_list():
    pass
