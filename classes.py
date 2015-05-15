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
    #    try??
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


    def make_average_rating(self):
        total = 0.00
        num_reviews = len(self.rating_list)
        for a in range(num_reviews):
            total += self.rating_list[a][1]
        self.average_rating = round((total/num_reviews), 2)






##def create movie to call all three of above??
##def create movie list to call create movie on all movies in list? (maybe put
##that into interface)

    #    except:
    #    if movie_rating hasn't been created?
