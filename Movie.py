from math import sqrt
from operator import attrgetter, itemgetter


class ShapeException(Exception):
    pass


class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def __str__(self):
        return "For the movie {} the average rating is {}.".\
                format(self.movie_title, self.average_rating)

    def movie_title(self, movie_names_dict):
        self.movie_title = movie_names_dict[self.movie_id]

    def movie_ratings_and_average(self, movie_id_dict):
        self.movie_rating = movie_id_dict[self.movie_id]

        total = 0.0
        for i in range(len(self.movie_rating)):
                total += self.movie_rating[i][1]
                self.average_rating = round((total/len(self.movie_rating)), 2)


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_sim_dict = {}

    def rating_list(self, user_id_dict):
        self.user_rating = user_id_dict[self.user_id]

        total = 0.0
        for i in range(len(self.user_rating)):
                total += self.user_rating[i][1]
                self.user_average = round((total/len(self.user_rating)), 2)

    def rating_dict(self, user_id_dict):
        self.user_rating_dict = {}
        for i in self.user_rating:
            self.user_rating_dict.setdefault(i[0], i[1])


    def __str__(self):
        return "User: {}, has reviewed {} movies with an average rating of {}"\
        .format(self.user_id, len(self.user_rating), self.user_average)

    def movies_reviewed(self):
        """ """
        movies_ratings = []
        for i in self.user_rating:
            movies_ratings.append(i[0])
            self.movies_rated = movies_ratings

    def compare_user_reviews(self, other):
        movies_in_common = []
        movies_not_in_common = []

        for i in self.movies_rated:
            if i in other.movies_rated:
                movies_in_common.append(i)
                self.common_movies = movies_in_common

        for i in other.movies_rated:
            if i not in self.movies_rated:
                movies_not_in_common.append(i)
                self.not_in_common_movies = movies_not_in_common

    def make_common_vectors(self, other):
        vector_self = []
        vector_other = []
        for i in self.common_movies:
            # for i in self.user_rating_dict:
            vector_self.append(self.user_rating_dict[i])
            vector_other.append(other.user_rating_dict[i])
        return vector_self, vector_other

    def create_similarity(self, other):
        v1, v2 = self.make_common_vectors(other)
        similarity = calculate_similarity(v1, v2)
        self.user_sim_dict.setdefault(other.user_id, similarity)

    def top_similar_users(self):
        sorted_list = sorted(self.user_sim_dict.items(), key=lambda x: x[1], reverse=True)
        self.top_similar_users = sorted_list
        return self.top_similar_users

    def movies_not_seen(self, other):
        self.uncommon_dict = {}
        for i in self.not_in_common_movies:
            self.uncommon_dict.setdefault(i, other.user_rating_dict[i])

    def top_similar_movies(self, other, length=5):
        #prints as a list of tuples
        top_uncommon_movies = sorted(self.uncommon_dict.items(),\
                                     key=lambda x: x[1], reverse=True)
        #calling 0-6 will give key of tuples
        top_uncommon_movies_list = [top_uncommon_movies[i][0] for i in range(length)]
        return top_uncommon_movies_list



#this is outside the class
def calculate_similarity(v1, v2, common=5):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """
    # Guard against empty lists.
    if len(v1) <= common:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v1[i] - v2[i] for i in range(len(v1))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return round(1 / (1 + sqrt(sum_of_squares)), 3)
