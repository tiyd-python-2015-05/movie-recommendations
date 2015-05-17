from operator import itemgetter
import math


class Recommender:
    def __init__(self, ratings, movie_filter=5, user_filter=3):
        self.ratings = ratings
        self.movie_filter = movie_filter
        self.user_filter = user_filter

    @property
    def movie_avgs(self):
        averages = []
        for movie in self.ratings.movie_table:
            averages.append([movie.ID, self.ratings.ratings_avg(movie.ID)])
        return averages

    def double_sort(self, a_list):
        double_sorted = sorted(a_list, key=itemgetter(0))
        double_sorted = sorted(double_sorted, key=itemgetter(1), reverse=True)
        return double_sorted

    @property
    def top(self):
        filtered_averages = []
        for movie in self.movie_avgs:
            if len(self.ratings.get_ratings(movie[0])) >= self.movie_filter:
                movie[0] = self.ratings.movie_title(movie[0])
                movie[1] = round(movie[1], 2)
                filtered_averages.append(movie)
        top_movies = self.double_sort(filtered_averages)

        return top_movies

    def topx(self, cut_off=10):
        return self.top[:cut_off]

    def bottomx(self, cut_off=10):
        return self.top[-cut_off:]

    def topx_for_user(self, user, cut_off=10):
        user_movies = [rating[0]
                       for rating in self.ratings.get_user_ratings(user)]

        top_unseen_movies = [movie for movie in self.top
                             if movie[0] not in user_movies]

        return top_unseen_movies[:cut_off]

    def user_match(self, user1, user2):
        user1_ratings = user1
        user2_ratings = user2
        # user1_ratings = self.ratings.get_user_ratings(user1)
        # user2_ratings = self.ratings.get_user_ratings(user2)
        # shared_ratings = []
        comparison = {rating[0] for rating in user1_ratings}
        user1_ratings = [rating[1] for rating in user1_ratings]
        user2_ratings = [rating[1] for rating in user2_ratings if rating[0] in comparison]

        # return user1_ratings, user2_ratings
        shared_ratings = zip(user1_ratings, user2_ratings)
        # for rating1 in user1_ratings:
        #     for rating2 in user2_ratings:
        #         if rating1[0] == rating2[0]:
        #             shared_ratings.append((rating1, rating2))
        return list(shared_ratings)

    def pearson_score(self, user1, user2):
        if len(self.user_match(user1, user2)) < self.user_filter:
            return 0

        user1_ratings, user2_ratings = zip(*self.user_match(user1, user2))

        user1_ratings = list(user1_ratings)
        user2_ratings = list(user2_ratings)

        covariance = sum([(x - (sum(user1_ratings)/len(user1_ratings))) *
                          (y - (sum(user2_ratings)/len(user2_ratings)))
                          for x, y in zip(user1_ratings, user2_ratings)])

        user1_deviation = math.sqrt(
            sum([(x - (sum(user1_ratings)/len(user1_ratings)))**2
                for x in user1_ratings]))

        user2_deviation = math.sqrt(
            sum([(y - (sum(user2_ratings)/len(user2_ratings)))**2
                for y in user2_ratings]))

        deviation_product = user1_deviation * user2_deviation

        if deviation_product == 0:
            return 0

        pearson_coefficient = covariance/deviation_product
        return pearson_coefficient

    def euclidean_distance(self, user1, user2):
        if len(self.user_match(user1, user2)) < self.user_filter:
            return 0

        user1_ratings, user2_ratings = zip(*self.user_match(user1, user2))

        user1_ratings = list(user1_ratings)
        user2_ratings = list(user2_ratings)

        differences = [user1_ratings[idx] - user2_ratings[idx]
                       for idx in range(len(user1_ratings))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)

        return 1 / (1 + math.sqrt(sum_of_squares))

    def similarity_score(self, user, user_list, function):
        users = user_list
        similar_users = []
        recommendations = []
        user_movies = [rating[0] for rating in self.ratings.get_user_ratings(user[0])]
        for userID in users:
            if userID[0] != user[0]:
                similarity = function(user[1], userID[1])
                similar_users.append([userID[0], similarity])
        similar_users = sorted(similar_users, key=itemgetter(1), reverse=True)

        for userID in similar_users[:10]:
            movies = self.ratings.get_user_ratings(userID[0])
            for movie in movies:
                if movie[0] not in [rating for rating in user_movies]:
                    recommendations.append([movie[0], (userID[1] * movie[1])])
        if len(recommendations) == 0:
            return 0
        return self.double_sort(recommendations)

    def user_recommendation(self, user, cut_off=10, pearson=True):
        # users = list(self.ratings.user_table.keys())
        users = [[key, self.ratings.user_table[key]] for key in self.ratings.user_table]
        input_user = [user, self.ratings.user_table[user]]
        if pearson:
            function = self.pearson_score
        else:
            function = self.euclidean_distance
        ordered_recommendations = \
            self.similarity_score(input_user, users, function)
        movie_recommendations = []
        for movie in ordered_recommendations:
            if movie[0] not in movie_recommendations:
                movie_recommendations.append(movie[0])

        return movie_recommendations[:cut_off]
