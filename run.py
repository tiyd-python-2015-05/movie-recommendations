from loader import load
from movies import Frame
from driver import Driver

import random
import os


class Run:
    def __init__(self):
        a, b, c = load()
        self.frame = Frame(a, b, c)

        self.commands = {'u': 'Print 5 random users', 'q': 'Quit Program',
                         'a': 'Find movie by ID',
                         'b': 'Average rating by movie ID',
                         't': 'Top 5 movies', 's': 'Most similar users',
                         'r': 'Recommend movies by user ID',
                         'm': 'Print 5 random movie IDs',
                         'n': 'Recommend movie by movie ID'}

    def loop(self):
        os.system('clear')
        while True:
            print("Command list: ")
            for item, value in self.commands.items():
                print("{}: {}".format(item, value))
            inp = input("Enter command: ")

            if inp.lower()[0] == 'q':
                break

            if inp.lower()[0] == 'u':
                os.system('clear')
                self.print_users()

            if inp.lower()[0] == 'a':
                inp = input("Movie ID: ")
                if inp.isdigit():
                    os.system('clear')
                    print(self.movies_id(int(inp)))

            if inp.lower()[0] == 'b':
                inp = input("Movie ID: ")
                if inp.isdigit():
                    os.system('clear')
                    print(round(self.avg_rating(int(inp)), 2))

            if inp.lower()[0] == 't':
                os.system('clear')
                print("Top 5 movies: ")
                print(self.top_5())

            if inp.lower()[0] == 's':
                os.system('clear')
                self.distance()

            if inp.lower()[0] == 'r':
                os.system('clear')
                self.recommend()

            if inp.lower()[0] == 'n':
                os.system('clear')
                self.recommend_by_movie()

            if inp.lower()[0] == 'm':
                os.system('clear')
                print(self.movies())

    def top_5(self):
        return self.frame.top_movies()

    def movies(self):
        return [random.choice(list(self.frame.names.keys())) for _ in range(5)]

    def print_users(self):
        print([random.choice(list(self.frame.users.keys())) for _ in range(5)])

    def movies_id(self, mid):
        return self.frame.name_by_id(mid)

    def avg_rating(self, mid):
        return self.frame.average_by_id(mid)[0]

    def distance(self):
        uid = input("User ID: ")
        dist = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]
        while dist != 'e' and dist != 'p':
            dist = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]

        if dist == 'e':
            dist = self.frame.e_distance
        else:
            dist = self.frame.p_distance

        if uid.isdigit():
            os.system('clear')
            print("Closest users to user {}:".format(uid))
            for item in self.frame.find_closest(int(uid), dist):
                print(item[0])
        else:
            print("No user with that ID found")

    def recommend(self):
        uid = input("User ID: ")
        distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]
        while distance != 'e' and distance != 'p':
            distance = input("By what metric? (E)uclidean, \
                             (P)earson: ").lower()[0]

        if distance == 'e':
            distance = self.frame.e_distance
        else:
            distance = self.frame.p_distance

        if uid.isdigit():
            os.system('clear')
            print("Movie Recommendations for user {}:".format(uid))
            movies = self.frame.find_rec_user(int(uid), distance)
            for movie in movies:
                print("{}".format(movie))
        else:
            print("No user with that ID found")

    def recommend_by_movie(self):
        mid = input("Movie ID: ")
        distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]
        while distance != 'e' and distance != 'p':
            distance = input("By what metric? (E)uclidean, \
                             (P)earson: ").lower()[0]

        if distance == 'e':
            distance = self.frame.movie_e_distance
        else:
            distance = self.frame.movie_p_distance

        if mid.isdigit():
            os.system('clear')
            print("Movie Recommendations from movie {}:".format(mid))
            movies = self.frame.find_closest_movies(int(mid), distance)
            for movie in movies:
                print("{}".format(movie))
        else:
            print("No movie with that ID found")


if __name__ == '__main__':
    run = Run()
    run.loop()
