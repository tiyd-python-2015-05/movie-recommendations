from recommend import *
from pprint import pprint as pprint

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

# def load_files():
#     users = User.load_users('datasets/ml-100k/uhead.user')
#     users = User.load_ratings('datasets/ml-100k/uhead.data', users)
#     movies = Movie.load_movies('datasets/ml-100k/uhead.item')
#     movies = Movie.load_ratings('datasets/ml-100k/uhead.data', movies)
#     return users, movies

def test_db_creation():
    db = DataBase(users_file='datasets/ml-100k/uhead.user',
                  movies_file='datasets/ml-100k/uhead.item',
                  ratings_file='datasets/ml-100k/uhead.data')
    assert db.users['1'].ratings['113'] == '5'
    assert db.movies['7'].avg_rating == 3.6
    assert db.movies['1'].movie_title == 'Toy Story (1995)'

def test_top_n():
#    users, movies = load_files()
#    pprint(movies.top_n(n=20, min=2, user=None))
    pass
