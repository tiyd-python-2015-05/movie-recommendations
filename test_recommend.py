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

def test_load_ratings():
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
