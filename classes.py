from math import sqrt
from operator import attrgetter, itemgetter

class ShapeException(Exception):
    pass

def calculate_similarity(vector1, vector2, min_reviews_in_common=5):
    if len(vector1) != len(vector2):
        raise ShapeException("Vectors must be same shape.")
    elif len(vector1) < min_reviews_in_common:
        return 0
    else:
        differences = [vector1[i] - vector2[i] for i in range(len(vector1))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)
        return round(1 / (1 + sqrt(sum_of_squares)), 3)




class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id
#        self.movie_title = movie_title
#        self.ratings = ratings


    def __str__(self):
        average_rounded = round(self.average_rating, 2)
        return ("{} is at ID # {} and has an average rating of {}"\
                .format(self.movie_title, self.movie_id, average_rounded))


    def make_title(self, movie_names_dict):
        self.movie_title = movie_names_dict[self.movie_id]


    def make_ratings(self, movie_rating_dict):
        self.movie_rating = movie_rating_dict[self.movie_id]


    def make_movie_average_rating(self):
        total = 0.00
        num_reviews = len(self.movie_rating)
        for a in range(num_reviews):
            total += self.movie_rating[a][1]
        self.average_rating = round((total/num_reviews), 2)


class User:
    def __init__(self, user_id):
        self.user_id = user_id


    def __str__(self):
        return ("User {} has made these ratings: (MovieID, rating): {}".format(self.user_id, self.rating_list))


    def make_ratings(self, user_rating_dict):
        self.rating_list = user_rating_dict[self.user_id]
        self.user_sim_dict = {}


    def make_ratings_dict(self):
        ratings_dict = {}
        for i in self.rating_list:
            ratings_dict[i[0]] = (i[1])
        self.ratings_dict = ratings_dict


    def make_average_rating(self):
        total = 0.00
        num_reviews = len(self.rating_list)
        for a in range(num_reviews):
            total += self.rating_list[a][1]
        self.average_rating = round((total/num_reviews), 2)


    def movies_reviewed(self):
        movie_list = []
        for i in self.rating_list:
            movie_list.append(i[0])
        self.movies_list = movie_list

    def make_common_reviews(self, other):
        """Returns a list of movies self and other have both reviewed"""
        movies_in_common = []
        for i in self.movies_list:
            if i in other.movies_list:
                movies_in_common.append(i)
        return movies_in_common

    def make_uncommon_reviews(self, other):
        """Returns list of movies other has reviewed that self has not"""
        movies_uncommon = []
        for i in other.movies_list:
            if i in self.movies_list:
                pass
            else:
                movies_uncommon.append(i)
        return movies_uncommon

    def make_ratings_vectors(self, other):
        common_movies = self.make_common_reviews(other)
        vector_self = []
        vector_other = []
        for i in common_movies:
            vector_self.append(self.ratings_dict[i])
            vector_other.append(other.ratings_dict[i])
        return vector_self, vector_other

    def create_similarity_score(self, other):
        (v_self, v_other) = self.make_ratings_vectors(other)
        similarity = calculate_similarity(v_self, v_other)
        self.user_sim_dict[other.user_id] = similarity
        return similarity
        #need to return??

    def create_top_users_in_common(self, length_list=3):
        sort_dict = self.user_sim_dict
        sort_list = sorted(sort_dict.items(), key=lambda x: x[1], reverse=True)
        top = sort_list[0:length_list]
        #this will return tuples of user and similarity score
        return top

    def movies_reviewed_not_seen(self, other, length_list=5):
        uncommon_list = self.make_uncommon_reviews(other)
        uncommon_dict = {}
        for i in uncommon_list:
            uncommon_dict[i] = other.ratings_dict[i]
        sort_uncommon = sorted(uncommon_dict.items(), key=lambda x:x[1],
                        reverse=True)

        top = sort_list[0:length_list]
        return top













##def create movie to call all three of above??
##def create movie list to call create movie on all movies in list? (maybe put
##that into interface)

    #    except:
    #    if movie_rating hasn't been created?
