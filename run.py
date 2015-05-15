from loader import load
from movies import Frame
from driver import Driver

import random
import os

class Run:
    def __init__(self):
        a,b = load()
        self.frame = Frame(a,b)
        self.driver = Driver(self.frame)
        self.commands = {'u':'Print 5 random users', 'q': 'Quit Program', 'a': 'Find movie by ID',
                         'b': 'Average rating by movie ID', 't': 'Top 5 movies',
                         's': 'Most similar users', 'r': 'Recommend movies by user ID'}
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
                if isinstance(inp, int):
                    os.system('clear')
                    print(self.movies_id(inp))

            if inp.lower()[0] == 'b':
                inp = input("Movie ID: ")
                os.system('clear')
                if isinstane(inp, int):
                    print(self.avg_rating(inp))

            if inp.lower()[0] == 't':
                os.system('clear')
                print("Top 5 movies: ")
                print(self.frame.top_movies())

            if inp.lower()[0] == 's':
                os.system('clear')
                self.distance()

            if inp.lower()[0] == 'r':
                os.system('clear')
                self.recommend()

    def print_users(self):
        print([random.choice(self.frame.users()) for _ in range(5)])

    def movies_id(self, mid):
        self.frame.name_by_id(mid)

    def avg_rating(self, mid):
        print(self.frame.average_by_id(mid))

    def distance(self):
        uid = input("User ID: ")
        distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]
        while distance != 'e' and distance != 'p':
            distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]

        if distance == 'e':
            distance = self.driver.e_distance
        else:
            distance = self.driver.p_distance

        if uid.isdigit():
            os.system('clear')
            print("Closest users to user {}:".format(uid))
            print(self.driver.find_closest(int(uid), distance))
        else:
            print("No user with that ID found")

    def recommend(self):
        uid = input("User ID: ")
        distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]
        while distance != 'e' and distance != 'p':
            distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]

        if distance == 'e':
            distance = self.driver.e_distance
        else:
            distance = self.driver.p_distance

        if uid.isdigit():
            os.system('clear')
            print("Movie Recommendations for user {}:".format(uid))
            movies = self.driver.find_rec(int(uid), distance)
            for movie in movies:
                print("{}".format(movie))
        else:
            print("No user with that ID found")

if __name__ == '__main__':
    run = Run()
    run.loop()
