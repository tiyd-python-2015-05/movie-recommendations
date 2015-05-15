class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id

    def movie_title(self, movie_names_dict):
        self.movie_title = movie_names_dict[self.movie_id]

    def movie_ratings_and_average(self, movie_id_dict):
        self.movie_rating = movie_id_dict[self.movie_id]

        total = 0.0
        for i in range(len(self.movie_rating)):
                total += self.movie_rating[i][1]
                self.average_rating = (total/len(self.movie_rating))

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def rating_list(self, user_id_dict):
        self.user_rating = user_id_dict[self.user_id]
