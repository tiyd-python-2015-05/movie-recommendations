from loader import load

from math import sqrt


class Driver:

    def __init__(self, frame):
        self.frame = frame

    @property
    def e_distance(self):
        def distance(users):
            user1 = self.frame.movies_by_user(users[0])
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
        def distance(users):
            user1 = self.frame.movies_by_user(users[0])
            user2 = self.frame.movies_by_user(users[1])
            common = [item for item in user1 if item in user2]

            if common and len(common) > 1:
                user1_mean = sum(map(lambda x: user1[x], common))
                user2_mean = sum(map(lambda x: user2[x], common))

                diff1 = map(lambda x: (user1[x] - user1_mean)**2, common)
                diff2 = map(lambda x: (user2[x] - user2_mean)**2, common)
                sds = sqrt(sum(diff1)*sum(diff2)) * len(common)**2

                common = map(lambda x: (user1[x] - user1_mean)*(user2[x]-user2_mean)
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
        users = self.frame.users()
        users.remove(user)  # recuse yourself
        users = zip([user]*len(users), users) # (user1, userN)
        users = [(user[1], distance(user)) for user in users] # (userN, distance)
        users = sorted(users, key=lambda x: x[1])
        if len(users) > 5:
            users = users[:5]
        return users

    def find_rec_user(self, user, distance):
        users = self.find_closest(user, distance) # (user, similarity) top 5
        usr_movies = self.frame.movies_by_user(user)

        movie = {}
        movies = []
        for item in users:
            movie.update(self.frame.movies_by_user(item[0])) # {movie: rating}

            movies.extend([(mov[0], mov[1]* item[1]) for mov in movie.items()
                      if mov[0] not in usr_movies]) # (movie, metric)

        if len(users) > 5:
            movies = sorted(movies, key=lambda x: x[1])
        else:
            movies = sorted(movies, key=lambda x: x[1])

        movies = movies[:5]
        movies = [self.frame.name_by_id(mov[0]) for mov in movies]

        return movies

    @property
    def movie_e_distance(self):
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

                common = map(lambda x: (movie1[x] - movie1_mean)*(movie2[x]-movie2_mean)
                            / (sds), common)
                return sum(common)
            else:
                return 0

        return distance

    def find_closest_movies(self, movie, distance):
        """
        finds 5 closest movies
        returns as list of
        (umovie_id, distance)
        """
        movies = list(self.frame.names.keys())
        movies.remove(movie)  # recuse yourself
        movies = zip([movie]*len(movies), movies)
        movies = [(movie[1], distance(movie)) for movie in movies]
        movies = sorted(movies, key=lambda x: x[1])
        if len(movies) > 5:
            movies = movies[:5]
        return [self.frame.names[movie[0]] for movie in movies]
