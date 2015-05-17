import operator


class Data:

    def __init__(self, movie, data):
        self.movie = movie
        self.data = data


    def the_rating(self, movie_id):

        return [self.data[item] for item in self.data if item[1] == movie_id]

    def avg_rating(self, movie_id):

        return (round(sum(self.the_rating(movie_id))/len(self.the_rating(movie_id))),\
         len(self.the_rating(movie_id)))

    def movie_name(self, movie_id):

        return ''.join([self.movie[name] for name in self.movie if name == movie_id])

    def user_ratings(self, user_id):

        return [self.data[item] for item in self.data if item[0] == user_id]

    def top_rated(self, num_o_mov, min_num_rates):

        all_ratings = sorted([(self.movie[item], self.avg_rating(item)[0])\
             for item in self.movie if\
             self.avg_rating(item)[1] >= min_num_rates], key=operator.itemgetter(1))[-(num_o_mov):]

        return all_ratings

    def unseen_movies(self, user_id):

        seen_movies = [movie[1] for movie in self.data if user_id in movie]

        unseen_movies = []

        for movie in self.data:
            if movie[1] in unseen_movies:
                pass
            else:
                if movie[1] not in seen_movies:
                    unseen_movies.append(movie[1])

        return unseen_movies

    def suggested(self, user_id, num_o_mov, min_num_rates):

        ratings = sorted([(self.movie[item], self.avg_rating(item)[0])\
             for item in self.unseen_movies(user_id) if\
             self.avg_rating(item)[1] >= min_num_rates], key=operator.itemgetter(1), reverse=True)[-(num_o_mov):]

        return ratings
