from operator import itemgetter
from math import sqrt

class Frame:
    def __init__(self, names, movies_data, users_data):
            self.movies = movies_data
            self.users = users_data
            self.names = names

    def ratings_by_id(self, movie_id):
        """
        Returns a list all ratings for a given movie
        """
        if movie_id in self.movies:
            return [self.movies[movie_id][item] for item
                    in self.movies[movie_id]]

        else:
            return "No movies found with that ID"

    def average_by_id(self, movie_id):
        """
        calculates the average rating for a given movie
        """
        if movie_id in self.names:
            return sum(self.ratings_by_id(movie_id)) \
                / len(self.ratings_by_id(movie_id)),\
                len(self.ratings_by_id(movie_id))
        else:
            return "No movies found with that ID"

    def name_by_id(self, movie_id):
        """
        returns the name of the movie with the given ID if it is
        in the movie list
        """
        if movie_id in self.names:
            return self.names[movie_id]

        return "No movies found with that ID"

    def top_movies(self, k=5):
        averages = list(map(self.average_by_id, self.movies))
        averages = [item[0] for item in averages if item[1] >= 5]

        averages = sorted(zip(self.names, averages),
                          key=lambda x: x[1], reverse=True)

        return [self.names[entry[0]] for entry in averages[:k]]

    def movies_by_user(self, user_id):
        """
        returns dictionary with movie_id: rating
        by the given user
        """
        return {item: self.users[user_id][item] for item
                in self.users[user_id]}

    def users_by_movie(self, movie_id):
        return {item: self.movies[movie_id][item] for item in self.movies}

    @property
    def e_distance(self):
        """
        returns a Euclidean distance function
        for distance between users
        by ratings of common movies
        """

        def distance(*users):
            user1 = self.users[users[0]]
            user2 = self.users[users[1]]
            common = [item for item in user1 if item in user2]


            if common:
                common = map(lambda x: (user1[x] - user2[x])**2, common)
                return 1 / (1 + sqrt(sum(common)))

            else:
                return 0

        return distance

    @property
    def p_distance(self):
        """
        returns a function that calculates
        the Pearson correlation coefficient
        between the two users by ratings
        of common movies
        """

        def distance(*users):
            user1 = self.users[users[0]]
            user2 = self.users[users[1]]
            common = [item for item in user1 if item in user2]

            if common and len(common) > 1:
                user1_mean = sum(map(lambda x: user1[x], common))
                user2_mean = sum(map(lambda x: user2[x], common))

                diff1 = map(lambda x: (user1[x] - user1_mean)**2, common)
                diff2 = map(lambda x: (user2[x] - user2_mean)**2, common)
                sds = sqrt(sum(diff1)*sum(diff2)) * len(common)**2

                common = map(lambda x: (user1[x] -
                                        user1_mean)*(user2[x]-user2_mean)
                             / (sds), common)
                return sum(common)
            else:
                return 0

        return distance

    def find_closest(self, user, distance):
        """
        finds 5 closest users
        returns as list of
        (user_id, distance)
        """
        users_list = list(self.users.keys())
        users_list.remove(user)  # recuse yourself
        users = [(other, distance(user, other)) for other in users_list]
        users = [item for item in users if item[1] != 0]
        users = sorted(users, key=itemgetter(1))
        if len(users) > 5:
            users = users[:5]
        return users

    def find_rec_user(self, user, distance):
        """
        returns five recommendations for a user
        that they have not rated by
        using the given distance function
        to find users most similar
        """
        users = self.find_closest(user, distance)  # (user, similarity) top 5
        usr_movies = self.users[user]

        movie = {}
        movies = []
        for item in users:
            movie.update(self.users[item[0]])  # {movie: rating}

            movies.extend([(mov[0], mov[1] * item[1]) for mov in movie.items()
                          if mov[0] not in usr_movies])  # (movie, metric)

        if len(users) > 5:
            movies = sorted(movies, key=lambda x: x[1])
        else:
            movies = sorted(movies, key=lambda x: x[1])

        movies = movies[:5]
        movies = [self.name_by_id(mov[0]) for mov in movies]

        return movies

    @property
    def movie_e_distance(self):
        """
        returns a Euclidean distance function
        for distance between movies
        by ratings from common users
        """

        def distance(movies):
            movie1 = self.movies[movies[0]]
            movie2 = self.movies[movies[1]]
            common = [item for item in movie1 if item in movie2]

            if common:
                common = map(lambda x: (movie1[x] - movie2[x])**2, common)
                return 1 / (1 + sqrt(sum(common)))

            else:
                return 0

        return distance

    @property
    def movie_p_distance(self):
        """
        returns a function that calculates
        the Pearson correlation coefficient
        between the two movies by ratings
        from common users
        """

        def distance(movies):
            movie1 = self.movies[movies[0]]
            movie2 = self.movies[movies[1]]
            common = [item for item in movie1 if item in movie2]

            if common and len(common) > 1:
                movie1_mean = sum(map(lambda x: movie1[x], common))
                movie2_mean = sum(map(lambda x: movie2[x], common))

                diff1 = map(lambda x: (movie1[x] - movie1_mean)**2, common)
                diff2 = map(lambda x: (movie2[x] - movie2_mean)**2, common)
                sds = sqrt(sum(diff1)*sum(diff2)) * len(common)**2

                common = map(lambda x: (movie1[x] -
                                        movie1_mean)*(movie2[x]-movie2_mean)
                             / (sds), common)
                return sum(common)
            else:
                return 0

        return distance

    def find_closest_movies(self, movie_id, distance):
        """
        finds 5 closest movies to a given movie
        returns as list of (umovie_id, distance)
        """
        movies = list(self.names.keys())
        movies.remove(movie_id)  # recuse yourself
        movies = zip([movie_id]*len(movies), movies)
        movies = [(mov[1], distance(mov)) for mov in movies]
        movies = sorted(movies, key=lambda x: x[1])
        if len(movies) > 5:
            movies = movies[:5]
        return [self.names[mov[0]] for mov in movies]
