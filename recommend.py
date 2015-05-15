import csv
import math
import pprint


class User():
    def __init__(self, user_id='1', age='24', gender='M', job='technician', zipcode='85711'):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.job = job
        self.zipcode = zipcode
        self.ratings = {}
        #self.movies = []

    @classmethod
    def load_users(cls, filename):
        fieldnames = ['user_id','age','gender','job', 'zipcode']
        users = {}
        with open(filename, encoding="windows-1252") as file:
            reader = csv.DictReader(file, delimiter='|', fieldnames=fieldnames)
            for row in reader:
                user_id = row.pop('user_id')
                users[user_id] = User(**row)
        return users

    @classmethod
    def load_ratings(cls, filename, users):
        fieldnames = ['user_id','item_id','rating','timestamp']
        #ratings = {}
        with open(filename, encoding="windows-1252") as file:
            reader = csv.DictReader(file, delimiter='\t', fieldnames=fieldnames)
            for row in reader:
                user_id = row['user_id']
                item_id = row['item_id']
                rating = row['rating']
                try:
                    users[user_id].ratings[item_id] = rating
                except KeyError:
                    assert KeyError("That user_id does not exist")
        return users
    @property
    def movies(self):
        try:
            return [item_id for item_id in self.ratings]
                          #sorted ... key=lambda x: x[1])
        except:
            assert KeyError("No movies found for this user")

class Movie():
    item_fieldnames = \
        ['movie_id', 'movie_title', 'release_date', 'video_release_date',
        'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation',
        "Childrens", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
        'FilmNoir', 'Horror', 'Musical', 'Mystery', 'Romance', 'SciFi',
        'Thriller', 'War', 'Western']

    def __init__(self, **kwargs):
        for prop, val in kwargs.items():
            setattr(self, prop, val)
        self.ratings = {}

    @classmethod
    def load_movies(cls, filename):
        movies = {}
        with open(filename, encoding="windows-1252") as file:
            reader = csv.DictReader(file, delimiter='|', fieldnames=Movie.item_fieldnames)
            for row in reader:
                movie_id = row.pop('movie_id')
                movies[movie_id] = Movie(**row)
        return movies

    @classmethod
    def load_ratings(cls, filename, movies):
        fieldnames = ['user_id','item_id','rating','timestamp']
        #ratings = {}
        with open(filename, encoding="windows-1252") as file:
            reader = csv.DictReader(file, delimiter='\t', fieldnames=fieldnames)
            for row in reader:
                user_id = row['user_id']
                item_id = row['item_id']
                rating = row['rating']
                try:
                    movies[item_id].ratings[user_id] = rating
                except KeyError:
                    movies[item_id] = Movie(ratings={})
                    movies[item_id].ratings[user_id] = rating

                    #raise KeyError("That movie or user id does not exist")
        return movies

    @property
    def users(self):
        try:
            return [user_id for user_id in self.ratings]
        except:
            assert KeyError("No users found for this movie")

    @property
    def num_ratings(self):
        return len(self.ratings)

    @property
    def avg_rating(self):
        return sum([int(val) for val in self.ratings.values()]) / len(self.ratings)


class DataBase():
    def __init__(self, users_file, movies_file, ratings_file):
        my_users = User.load_users(users_file)
        my_users = User.load_ratings(ratings_file, my_users)
        my_movies = Movie.load_movies(movies_file)
        my_movies = Movie.load_ratings(ratings_file, my_movies)

        self.users = my_users
        self.movies = my_movies
        #self.ratings = {}

    def top_n(self, n=20, min_n=2, user=None):
        averages = {movie: self.movies[movie].avg_rating
                    for movie in self.movies
                    if self.movies[movie].num_ratings >= min_n}
        self.averages = []
        for item_id in sorted(averages, key=averages.get, reverse=True):
            self.averages.append((item_id, averages[item_id]))

        if user is None:
            return self.averages[:n]
        else:
            num_ratings = len(self.users[user].ratings)
            averages = self.averages[:n+num_ratings]
            averages = [avg for avg in averages if avg[0] not in self.users[user].movies]
            return averages[:n]
    def intersection(self, me, them):
        v = set(self.users[me].movies)
        w = set(self.users[them].movies)
        return list(v.intersection(w))
        #return [x for x in self.users[me].movies]

    def euclidean_distance(self, me, other):
        """Given two lists, give the Euclidean distance between them on a scale
        of 0 to 1. 1 means the two lists are identical.
        """
        s = self.users[me].ratings
        o = self.users[other].ratings
        ixn = self.intersection(me, other)

        v = []
        w = []

        for movie in ixn:
            #print(repr(movie))
            #print(self.users[me].ratings[movie])
            v.append(int(self.users[me].ratings[movie]))
            w.append(int(self.users[other].ratings[movie]))

        # Guard against empty lists.
        if len(v) is 0:
            return 0

        # Note that this is the same as vector subtraction.
        differences = [v[idx] - w[idx] for idx in range(len(v))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)

        return 1 / (1 + math.sqrt(sum_of_squares))


if __name__ == '__main__':
    db = DataBase(users_file='datasets/ml-100k/uhead.user',
                  movies_file='datasets/ml-100k/uhead.item',
                  ratings_file='datasets/ml-100k/uhead.data')
