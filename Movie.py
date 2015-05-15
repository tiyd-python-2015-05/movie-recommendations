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

    def rating_list(self, user_id_dict):
        self.user_rating = user_id_dict[self.user_id]

        total = 0.0
        for i in range(len(self.user_rating)):
                total += self.user_rating[i][1]
                self.user_average = round((total/len(self.user_rating)), 2)

    def __str__(self):
        return "User: {}, has reviewed {} movies with an average rating of {}"\
        .format(self.user_id, len(self.user_rating), self.user_average)
