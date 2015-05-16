from recommend import *
from pprint import pprint as pprint

def test_data_files_are_present():
    with open("datasets/ml-100k/u.data") as file:
        assert file.readline()
    with open("datasets/ml-100k/u.item") as file:
        assert file.readline()
    with open("datasets/ml-100k/u.user") as file:
        assert file.readline()

def test_user_creation():
    user = User(user_id='1', age='24', gender='M', job='technician', zipcode='85711')
    assert isinstance(user, User)
    assert user.zipcode == '85711'

def test_load_users():
    users = User.load_users('datasets/ml-100k/uhead.user')
    print(users)
    assert users['1'].job == 'technician'
    assert users['10'].zipcode == '90703'

def test_load_user_ratings():
    # cat u.data ',' egrep "^[1-9]\t" > uhead.data
    users = User.load_users('datasets/ml-100k/uhead.user')
    users = User.load_ratings('datasets/ml-100k/uhead.data', users)
    assert len(users['1'].ratings) == 272
    assert users['1'].ratings['113'] == '5'

def test_user_movies_property():
    users = User.load_users('datasets/ml-100k/uhead.user')
    users = User.load_ratings('datasets/ml-100k/uhead.data', users)
    for item_id in ['236', '180', '17']:
        assert item_id in users['1'].movies

def test_movie_creation():
    fieldnames = Movie.item_fieldnames
    values = ['1','Toy Story (1995)','01-Jan-1995','','http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)','0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0']
    kwargs = dict(zip(fieldnames, values))
    movie = Movie(**kwargs)
    assert isinstance(movie, Movie)
    print(dir(movie))
    assert movie.movie_id == '1'
    assert movie.Animation == '1'
    assert movie.movie_title == 'Toy Story (1995)'
    assert movie.Western == '0'

def test_load_movies():
    movies = Movie.load_movies('datasets/ml-100k/uhead.item')
    pprint(movies)
    assert movies['1'].movie_title == 'Toy Story (1995)'
    assert movies['1'].Animation == '1'

def test_load_movie_ratings():
    movies = Movie.load_movies('datasets/ml-100k/uhead.item')
    movies = Movie.load_ratings('datasets/ml-100k/uhead.data', movies)
    assert len(movies['7'].ratings) == 5
    pprint(movies['7'].ratings)
    assert movies['7'].ratings['9'] == '4'
    #pprint(movies)
    assert movies['127'].ratings['7'] == '5'

def test_movies_users_property():
    movies = Movie.load_movies('datasets/ml-100k/uhead.item')
    movies = Movie.load_ratings('datasets/ml-100k/uhead.data', movies)
    for user_id in ['2', '6', '5', '1']:
        assert user_id in movies['1'].users

def test_movies_num_ratings():
    movies = Movie.load_movies('datasets/ml-100k/uhead.item')
    movies = Movie.load_ratings('datasets/ml-100k/uhead.data', movies)
    assert movies['1'].num_ratings == 4

def test_movies_avg_rating():
    movies = Movie.load_movies('datasets/ml-100k/uhead.item')
    movies = Movie.load_ratings('datasets/ml-100k/uhead.data', movies)
    assert movies['7'].avg_rating == 3.6

def load_files():
#     users = User.load_users('datasets/ml-100k/uhead.user')
#     users = User.load_ratings('datasets/ml-100k/uhead.data', users)
#     movies = Movie.load_movies('datasets/ml-100k/uhead.item')
#     movies = Movie.load_ratings('datasets/ml-100k/uhead.data', movies)
#     return users, movies
    db = DataBase(users_file='datasets/ml-100k/uhead.user',
                  movies_file='datasets/ml-100k/uhead.item',
                  ratings_file='datasets/ml-100k/uhead.data')
    return db

def test_db_creation():
    db = load_files()
    assert db.users['1'].ratings['113'] == '5'
    assert db.movies['7'].avg_rating == 3.6
    assert db.movies['1'].movie_title == 'Toy Story (1995)'

# def test_db_avgs():
#     db = load_files()
#     for i in [('581', 5.0), ('313', 5.0), ('109', 5.0)]:
#         assert i in db.averages


def test_top_n():
    db = load_files()
    assert db.top_n(n=20, min_n=2, user=None)[0][1] == 5.0
    assert db.top_n(n=20, min_n=20, user=None) == []
    assert len(db.top_n(n=20, min_n=2, user=None)) == 20
    assert len(db.top_n(n=20, min_n=5, user=None)) == 14
    rankings = db.top_n(n=10, min_n=3, user=None)
    last = 5
    for i in rankings:
        assert last >= i[1]
        last = i[1]

def test_top_n_user():
    db = load_files()
    unfiltered = db.top_n(n=20, min_n=5, user=None)
    tup_list = db.users['1'].movies
    m_list = [m[0] for m in tup_list]
    print(m_list)
    filtered = db.top_n(n=20, min_n=4, user='1')
    assert len(unfiltered) > len(filtered)
    for (mov, avg) in filtered:
        assert mov not in db.users['1'].movies

def test_intersection():
    db = load_files()
    intersection = db.intersection('1', '2')
    for movie in intersection:
        assert movie in db.users['1'].movies
        assert movie in db.users['2'].movies

def test_euclidean_distance():
    db = load_files()
    dist = db.euclidean_distance('1', '2')
    print(dist)
    assert dist['dist'] - 0.1613 < 0.01

def test_num_items_test_files():
    db = load_files()
    assert len(db.users) == 10
    assert len(db.users['1'].ratings) == 272
    assert len(db.movies) == 691

def test_calculate_similarities():
    db = load_files()
    #pairings = db.calculate_similarities()
    #print(pairings, '\n Length: ', len(pairings))
    db.calculate_similarities()
    pprint(db.similarities)
    try:
        assert db.similarities[('9','8')]['dist'] - 0.1907 < 0.01
        assert db.similarities[('9','8')]['num_shared'] == 4
    except:
        assert db.similarities[('8','9')]['dist'] - 0.1907 < 0.01
        assert db.similarities[('8','9')]['num_shared'] == 4
    
def test_similar_users():
    db = load_files()
    db.calculate_similarities()
    pprint(db.similar('2','1', n=5, min_matches=3))
    #assert False
# def test_number_of_entries():
#     # Data from u.info
#     db = load_files()
#     assert len(db.users) == 943

"""
943 users
1682 items
100000 ratings
"""
