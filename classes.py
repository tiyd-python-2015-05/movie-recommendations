class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id
#        self.movie_title = movie_title
#        self.ratings = ratings


    def make_title(self, movie_names_dict):
        self.movie_title = movie_names_dict[self.movie_id]


    def make_ratings(self, movie_rating_dict):
        self.movie_rating = movie_rating_dict[self.movie_id]


    def make_movie_average_rating(self):
    #    try??
        total = 0.0
        num_reviews = len(self.movie_rating)
        for a in range(num_reviews):
            total += self.movie_rating[a][1]
        self.average_rating = total/num_reviews

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def make_ratings(self, user_rating_dict):
        self.rating_list = user_rating_dict[self.user_id]






##def create movie to call all three of above??
##def create movie list to call create movie on all movies in list? (maybe put
##that into interface)

    #    except:
    #    if movie_rating hasn't been created?
