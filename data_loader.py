import csv
from pprint import pprint as pprint



# u.user
"""
Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.
"""

def load_data(filename="datasets/ml-100k/u.data"):
    # u.data
    # user id | item id | rating | timestamp
    fieldnames = ['user_id','item_id','rating','timestamp']
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter='\t', fieldnames=fieldnames)
        ratings = Ratings()
        for row in reader:
            ratings.add_rating(**row)
        return ratings

def load_items(filename="datasets/ml-100k/u.item"):
    # u.item
    """
    movie id | movie title | release date | video release date |
    IMDb URL | unknown | Action | Adventure | Animation |
    Children's | Comedy | Crime | Documentary | Drama | Fantasy |
    Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
    Thriller | War | Western |
    """
    fieldnames = \
        ['movie id', 'movie title', 'release date', 'video release date',
        'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation',
        "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
        'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
        'Thriller', 'War', 'Western']

    with open(filename, encoding="windows-1252") as file:
        reader = csv.DictReader(file, delimiter='|', fieldnames=fieldnames)
        movies = Movies()
        for row in reader:
            #print(row)
            movies.add_movie(**row)
        return movies
        #row = next(reader)
        #movies.add_movie(**row)

class Ratings():
    def __init__(self):
        self._ratings = {}
        self._averages = {}
        # self._flat_ratings = {}

    def add_rating(self, user_id, item_id, rating, timestamp):
        current_ratings = self._ratings.setdefault(item_id,[])
        current_ratings.append({'user_id': user_id,
                                 'rating': rating,
                                 'timestamp': timestamp
                                })
        self._ratings[item_id] = current_ratings

    def show_item_ratings(self, item_id):
        num_ratings = len(self._ratings[item_id])
        print('Showing {} ratings for Item {}'.format(num_ratings, item_id))
        fieldnames = ['user_id','rating','timestamp']
        for item in fieldnames:
            print(item, ' ', end='')
        print('\n==========================')
        for i in self._ratings[item_id]:
            print('{user_id}\t   {rating}\t {timestamp}'.format(**i))
        # print(users._users['196'])

    def avg_rating(self, item_id):
        item_ratings = [int(r['rating']) for r in self._ratings[item_id]]
        avg_rating = sum(item_ratings)/len(item_ratings)
        return avg_rating
        #pprint(self._ratings[item_id])

    def user_ratings(self, user_id):
        my_ratings = []
        for item, ratings in self._ratings.items():
            for rating in ratings:
                if rating['user_id'] == user_id:
                    my_ratings.append({'movie': item, 'rating': rating['rating']})
        return my_ratings

    def calculate_averages(self, min_review_cutoff=5):
        averages = {}
        self._averages = []
        #for item_id in self._ratings:
        #    averages[item_id] = self.avg_rating(item_id)
        averages = {item: self.avg_rating(item) for item in self._ratings
                    if len(self._ratings[item]) > min_review_cutoff}
        for item_id in sorted(averages, key=averages.get, reverse=True):
            self._averages.append((item_id, averages[item_id]))

    def top_n(self, n, movies):
        top = []
        averages = self._averages[:n]
        for item in averages:
            top.append((movies.movie_title(item[0]), item[1]))
        return top

    # def get_ratings(self):
    #    return copy(self._ratings)

class Movies():
    def __init__(self):
        self._movies = {}
        # self._flat_ratings = {}

    def add_movie(self, **kwargs):
        movie_id = kwargs.pop('movie id')
        current_movies = self._movies.setdefault(movie_id,[])
        #print(movie_id, kwargs)
        current_movies.append({'movie title': kwargs['movie title'],
                                 'release date': kwargs['release date']
                                })
        self._movies[movie_id] = current_movies
    def show_movie(self, movie_id):
        pprint(self._movies[movie_id])
    def movie_title(self, movie_id):
        return self._movies[movie_id][0]['movie title']

if __name__ == '__main__':
    ratings = load_data()
    ratings.show_item_ratings('190')
    print('Average rating: ', ratings.avg_rating('1000'))
    movies = load_items()
    movies.show_movie('123')
    pprint(ratings.user_ratings('124'))
    pprint(movies.movie_title('123'))
    ratings.calculate_averages()
    pprint(ratings.top_n(20,movies))
