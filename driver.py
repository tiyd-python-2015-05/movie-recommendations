from math import sqrt
from operator import itemgetter


class Driver:

    def __init__(self, frame):
        self.frame = frame
        # trying various things to speed up
    #    self.u_pairs = {frozenset([item1, item2]) for item1
    #                    in self.frame.users for item2 in self.frame.users}
    #    self.m_pairs =  {frozenset([item1, item2]) for item1
    #                    in self.frame.names for item2 in self.frame.names}
    #    self.e_distances = {user: self.e_distance(user)
    #                        for user in self.u_pairs}
    #    self.p_distances = {user: self.p_distance(user)
    #                        for user in self.u_pairs}
    #    self.movie_e_distances = {movie: self.movie_e_distance(movie)
    #                              for movie in self.m_pairs}
    #    self.movie_p_distances = {movie: self.movie_p_distance(movie)
    #                              for movie in self.m_pairs}

    @property
    def e_distance(self):
        """
        returns a Euclidean distance function
        for distance between users
        by ratings of common movies
        """

        def distance(*users):
            user1 = self.frame.movies_by_user(users[0])  # movie, rating pairs
            user2 = self.frame.movies_by_user(users[1])
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
            user1 = self.frame.movies_by_user(users[0])
            user2 = self.frame.movies_by_user(users[1])
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
        users_list = self.frame.users[:]
        users_list.remove(user)  # recuse yourself
        users = [(other, distance(user, other)) for other in users_list]
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
        usr_movies = self.frame.movies_by_user(user)

        movie = {}
        movies = []
        for item in users:
            movie.update(self.frame.movies_by_user(item[0]))  # {movie: rating}

            movies.extend([(mov[0], mov[1] * item[1]) for mov in movie.items()
                          if mov[0] not in usr_movies])  # (movie, metric)

        if len(users) > 5:
            movies = sorted(movies, key=lambda x: x[1])
        else:
            movies = sorted(movies, key=lambda x: x[1])

        movies = movies[:5]
        movies = [self.frame.name_by_id(mov[0]) for mov in movies]

        return movies

    @property
    def movie_e_distance(self):
        """
        returns a Euclidean distance function
        for distance between movies
        by ratings from common users
        """

        def distance(movies):
            movie1 = self.frame.users_by_movie(movies[0])
            movie2 = self.frame.users_by_movie(movies[1])
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
            movie1 = self.frame.movies_by_user(movies[0])
            movie2 = self.frame.movies_by_user(movies[1])
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

    def find_closest_movies(self, movie, distance):
        """
        finds 5 closest movies to a given movie
        returns as list of (umovie_id, distance)
        """
        movies = list(self.frame.names.keys())
        movies.remove(movie)  # recuse yourself
        movies = zip([movie]*len(movies), movies)
        movies = [(mov[1], distance(mov)) for mov in movies]
        movies = sorted(movies, key=lambda x: x[1])
        if len(movies) > 5:
            movies = movies[:5]
        return [self.frame.names[mov[0]] for mov in movies]
