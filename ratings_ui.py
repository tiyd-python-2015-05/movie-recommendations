from loader import load
from movies import Frame

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
                diff2 = map(lambda x: (user1[x] - user1_mean)**2, common)
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
        users = zip([user]*len(users), users)
        users = [(user[1], distance(user)) for user in users]
        users = sorted(users, key=lambda x: x[1])
        if len(users) > 5:
            users = users[:5]
        return users

    def find_rec(self, user, distance):
        users = self.find_closest(user, distance) # (user, similarity) top 5
        usr_movies = self.frame.movies_by_user(user)
        for item in users:
            movie = self.frame.movies_by_user(item[0]) # {movie: rating}

            movie = [(mov[0], mov[1]* item[1]) for mov in movie.items()
                     if mov[0] not in usr_movies]

        if len(users) > 5:
            movie = sorted(movie, key=lambda x: x[1])[:5] # top 5
        else:
            movie = sorted(movie, key=lambda x: x[1])

        movie = [self.frame.name_by_id(mov[0]) for mov in movie]

        return movie
