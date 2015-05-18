import operator
import math

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

        return sorted([(item[1], self.data[item]) for item in self.data if item[0] == user_id], key=operator.itemgetter(0))


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

    def suggested(self, user_id, num_o_mov=5, min_num_rates=5):

        ratings = sorted([(self.movie[item], self.avg_rating(item)[0])\
             for item in self.unseen_movies(user_id) if\
             self.avg_rating(item)[1] >= min_num_rates], key=operator.itemgetter(1), reverse=True)[-(num_o_mov):]

        return ratings

    def similarity(self, user_id_1, user_id_2):

        # user_ratings
        u1 = self.user_ratings(user_id_1)
        u2 = self.user_ratings(user_id_2)

        differences = sorted([abs(x[1]-y[1]) for x in u1 for y in u2 if x[0]==y[0]])

        if differences == 0:
            return 0
        else:
            squares = [diff ** 2 for diff in differences]
            sum_of_squares = sum(squares)

        return round(1 / (1 + math.sqrt(sum_of_squares)),2)

    def recommendations(self,user_id, min_sim):

        similar_users = sorted([(user[1],\
                        round((self.data[user] * self.similarity(user_id, user[0])),1))\
                        for user in self.data if user_id != user[0]\
                        and user[1] in self.unseen_movies(user_id)\
                        and self.data[user] * self.similarity(user_id, user[0]) >= min_sim],\
                        key=operator.itemgetter(1))

        similar_users = sorted(dict(similar_users).items(),\
                        key= operator.itemgetter(1),\
                        reverse= True)

        return similar_users
