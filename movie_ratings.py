import csv
from operator import itemgetter


def dict_read_csv(filename, delimiter, *args):
    with open(filename, encoding="windows-1252") as file:
        reader = csv.DictReader(file, fieldnames=(args), delimiter=delimiter)
        data = []
        for row in reader:
            row = {key: row[key] for key in row if key != "Timestamp"}
            data.append(row)
        for item in data:
            for key in item:
                try:
                    item[key] = int(item[key])
                except:
                    pass
        return data


###############################################################################


class Movie:
    def __init__(self, dictionary):
        self.ID = dictionary["MovieID"]
        self.title = dictionary["Movie Title"]
        self.genre = self.get_genres(dictionary)

    def get_genres(self, dictionary):
        genres = {key
                  for key in dictionary
                  if dictionary[key] == 1 and
                  key not in ['MovieID', 'Movie Title', 'release date',
                              'video release date', 'IMDb URL']}
        return genres


###############################################################################


class Ratings:
    def __init__(self, movies, user_ratings):
        self.movie_table = self.make_movie_ratings_dict(movies, user_ratings)
        self.user_table = self.make_user_ratings_dict(movies, user_ratings)

    def make_movie_ratings_dict(self, movies, user_ratings):
        users = {}

        for rating in user_ratings:
            users[rating["MovieID"]] = users.get(rating["MovieID"], [])
            users[rating["MovieID"]].append([rating["User"], rating["Rating"]])

        movie_table = {Movie(mov): users[mov["MovieID"]] for mov in movies}

        return movie_table

    def make_user_ratings_dict(self, movies, user_ratings):
        users = {}

        for rating in user_ratings:
            users[rating["User"]] = users.get(rating["User"], [])
            users[rating["User"]].append([rating["MovieID"], rating["Rating"]])

        return users

    def get_ratings(self, movie):
        for key in self.movie_table:
            if key.ID == movie:
                return [item[1] for item in self.movie_table[key]]

    def ratings_avg(self, movie):
        for key in self.movie_table:
            if key.ID == movie:
                ratings = [item[1] for item in self.movie_table[key]]
                return sum(ratings)/len(ratings)

    def movie_title(self, movie):
        for key in self.movie_table:
            if key.ID == movie:
                return key.title

    def movie_ID(self, movie):
        for key in self.movie_table:
            if key.title == movie:
                return key.ID

    def get_user_ratings(self, user):
        rating_list = []
        for key in self.user_table:
            if key == user:
                rating_list = self.user_table[key]
        title_ratings = [[self.movie_title(entry[0]), entry[1]] for entry in rating_list]
        return sorted(title_ratings, key=itemgetter(0))
