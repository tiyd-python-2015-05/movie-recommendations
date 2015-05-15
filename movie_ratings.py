import csv


# def read_csv(filename, delimiter):
#     with open(filename, encoding="windows-1252") as file:
#         reader = csv.reader(file, delimiter=delimiter)
#         data = [row for row in reader]
#         return data


def dict_read_csv(filename, delimiter, *args):
    with open(filename, encoding="windows-1252") as file:
        reader = csv.DictReader(file, fieldnames=(args), delimiter=delimiter)
        data = [row for row in reader]
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
                  if dictionary[key] == "1" and
                  key not in ['MovieID', 'Movie Title', 'release date',
                              'video release date', 'IMDb URL']}
        return genres


###############################################################################


class Ratings:
    def __init__(self, movies, user_ratings):
        self.table = self.make_ratings_dict(movies, user_ratings)

    def make_ratings_dict(self, movies, user_ratings):
        table = {Movie(mov): [[user[key] for key in sorted(user, reverse=True)
                               if key not in ["Timestamp", "MovieID"]]
                              for user in user_ratings
                              if user["MovieID"] == mov["MovieID"]]
                 for mov in movies}
        return table

    def get_ratings(self, movie):
        for key in self.table:
            if key.ID == movie:
                return [item[1] for item in self.table[key]]

    def ratings_avg(self, movie):
        for key in self.table:
            if key.ID == movie:
                ratings = [int(item[1]) for item in self.table[key]]
                return str(sum(ratings)/len(ratings))

    def movie_title(self, movie):
        for key in self.table:
            if key.ID == movie:
                return key.title

    def get_user_ratings(self, user):
        ratings = []
        for key in self.table:
            for rating in self.table[key]:
                if rating[0] == str(user):
                    ratings.append([key.title, rating[1]])
        return sorted(ratings)
