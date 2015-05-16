class ShapeException(Exception):
    pass

def calculate_similarity(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ShapeException("Vectors must be same shape.")
    elif len(vector1) == 0:
        return 0
    else:
        similarity = 1
        return similarity



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










##def create movie to call all three of above??
##def create movie list to call create movie on all movies in list? (maybe put
##that into interface)

    #    except:
    #    if movie_rating hasn't been created?
