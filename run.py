from loader import load
from movies import Frame
from ratings_ui import Driver

import random
import os

class Run:
    def __init__(self):
        a,b = load()
        self.frame = Frame(a,b)
        self.driver = Driver(self.frame)
        self.commands = {'u':'Print Users', 'q': 'Quit Program', 'a': 'Find movie by ID',
                         'b': 't': 'Top 5 movies', 's': 'Most similar users'}
    def loop(self):
        while True:
            print("Command list: {}".format(commands))
            inp = input("Enter command: ")

            if inp.lower()[0] == 'q':
                break

            if inp.lower()[0] == 'u':
                self.print_users()

            if inp.lower()[0] == 'a':
                inp = input("Movie ID: ")
                if isinstance(inp, int)
                    print(self.movies_id(inp))

            if inp.lower()[0] == 'b':
                inp = input("Movie ID: ")
                if isinstane(inp, int):
                    print(self.avg_rating(inp))

            if inp.lower()[0] == 't':
                print(self.frame.top_movies())

            if inp.lower()[0] == 's':
                uid = input("User ID: ")
                distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]
                while distance != 'e' or distance != 'p':
                    distance = input("By what metric? (E)uclidean, (P)earson: ").lower()[0]

                if distance == 'e':
                    distance = self.driver.e_distance
                else:
                    distance = self.driver.p_distance

                if isinstance(uid, int):
                    os.system('clear')
                    print(self.driver.find_closest(uid))
                else:
                    print("No user with that ID found")



    def print_users(self):
        print([random.choice(self.frame.users()) for _ in range(5)])

    def movies_id(self, mid):
        self.frame.name_by_id(mid)

    def avg_rating(self, mid):
        print(self.frame.average_by_id(mid))

if __name__ == '__main__':
    run = Run()
    run.loop()
