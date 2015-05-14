import csv
import random
import functools


class RatingException(Exception):
    pass

@functools.total_ordering
class Movie:
    def __init__(self, title, rd, video_rd, url):
        self.title = title
        self.rd = rd
        self.video_rd = video_rd
        self.url = url
        self.genre = []
        self.ratings = {}

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.avg() == other.avg()

    def __lt__(self, other):
        return self.avg() < other.avg()

    def add_genre(self, text):
        self.genre.append(text)

    def add_rating(self, user_id, rating):
        self.ratings[user_id] = rating

    def list_scores(self):
        return list(self.ratings.values())

    def avg(self):
        lval = self.list_scores()
        return sum(lval)/len(lval)


class User:
    def __init__(self):
        self.ratings = {}

    def __str__(self):
        rt_st = "reviewed "+str(len(self.ratings)).rjust(4)+" movies, "
        rt_st += " avg score of "+str(round(self.avg(),2))+" stars, "
        rt_st += " std of "+str(round(self.std(),2))+" stars"
#        for label in self.ratings:
#            rt_st += "   "+self.ratings[label]
        return rt_st

    def list_scores(self):
        return list(self.ratings.values())

    def avg(self):
        lval = self.list_scores()
#        print(lval)
        return sum(lval)/len(lval)

    def std(self):
        lval = self.list_scores()
        mean = self.avg()
        return sum((i-mean)**2 for i in lval)**(0.5)/len(lval)

    def add_rating(self, movie_id, rating):
        self.ratings[movie_id] = rating


user_key = ["user id", "item id", "rating", "timestamp"]
movie_key = ["movie id", "movie title", "release date", "video release date",
"IMDb URL", "unknown", "Action", "Adventure", "Animation",
"Children's", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
"Film-Noir", "Horror", "Musical", "Mystery", "Romance", "Sci-Fi",
"Thriller", "War", "Western"]


movie_dict = {}
with open("ml-100k/u.item") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        props_dict = {}
        for i in range(len(movie_key)):
            props_dict[movie_key[i]] = row[i]
#        if sum(int(row[i]) for i in range(5,len(movie_key))) > 1:
#            print(" multipule genre flag triggered ")
#            print(row)
#        i = 5
#        print(props_dict)
#        while int(row[i]) == 0:
#            i += 1
#        genre = row[i]
        movie = Movie(props_dict["movie title"], props_dict["release date"],
                      props_dict["video release date"],
                      props_dict["IMDb URL"])
        for i in range(5,len(props_dict)):
            if int(row[i]) == 1:
                movie.add_genre(row[i])
        movie_dict[int(props_dict["movie id"])] = movie
print(movie)
print(" ")
print(" 10 random movies ")
for i in range(10):
    tag = random.choice(list(movie_dict.keys()))
    print(str(tag) + " " + str(movie_dict[tag]))


user_dict = {}
with open("ml-100k/u.data") as file:
    for line in file:
        user_vals = line.split()
        user_vals = [int(x) for x in user_vals]
        user_id     = user_vals[0]
        movie_id    = user_vals[1]
        rating      = user_vals[2]
        timestamp   = user_vals[3]
        if user_id not in user_dict:
            user_dict[user_id] = User()
        user_dict[user_id].add_rating(movie_id, rating)
        movie_dict[movie_id].add_rating(user_id, rating)

#print(list(user_dict[1].ratings.values()))
print(" ")
print(" 10 random users")
for row in range(10):
    tag = random.choice(list(user_dict.keys()))
    print(user_dict[tag])

print(" 10 top rated movies ")
top10 = sorted(movie_dict, key=movie_dict.get, reverse=True)[:10]
for i in range(10):
    movie = movie_dict[top10[i]]
    print(str(movie)+" "+str(movie.ratings))
