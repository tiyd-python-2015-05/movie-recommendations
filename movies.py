import csv
import random
import functools
import math


class RatingException(Exception):
    pass

exclude = False
current_user = None

@functools.total_ordering
class Movie:
    def __init__(self, idVal, title, rd, video_rd, url):
        self.idVal = idVal
        self.title = title
        self.rd = rd
        self.video_rd = video_rd
        self.url = url
        self.genre = []
        self.rate_val = {}
        self.rate_obj = {}

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.idVal == other.idVal
#        return self.avg_cutoff() == other.avg_cutoff()

    def __lt__(self, other):
        if self.avg_cutoff() == other.avg_cutoff():
            return self.idVal < other.idVal
        else:
            return self.avg_cutoff() < other.avg_cutoff()

    def add_genre(self, text):
        self.genre.append(text)

    def add_rating(self, user_id, user, rating):
        self.rate_val[user_id] = rating
        self.rate_obj[user_id] = user

    def list_scores(self):
        return list(self.rate_val.values())

    def avg(self):
        lval = self.list_scores()
        return sum(lval)/len(lval)

    def avg_cutoff(self):
        lval = self.list_scores()
        ans = sum(lval)/len(lval)
        if len(lval) < 5: # few reviews, send to bottom of list
            return 0
        if exclude and self.idVal in current_user.rate_val.keys():
            return 0
        return ans


class User:
    def __init__(self, idVal):
        self.id = idVal
        self.rate_val = {}
        self.rate_obj = {}

    def __str__(self):
        rt_st = "reviewed "+str(len(self.rate_val)).rjust(4)+" movies, "
        rt_st += " avg score of "+str(round(self.avg(),2))+" stars, "
        rt_st += " std of "+str(round(self.std(),2))+" stars"
        return rt_st

    def list_scores(self):
        return list(self.rate_val.values())

    def avg(self):
        lval = self.list_scores()
#        print(lval)
        return sum(lval)/len(lval)

    def std(self):
        lval = self.list_scores()
        mean = self.avg()
        return sum((i-mean)**2 for i in lval)**(0.5)/len(lval)

    def add_rating(self, movie_id, movie, rating):
        self.rate_val[movie_id] = rating
        self.rate_obj[movie_id] = movie

    def movie_hist(self):
        rt_st = ""
        for movie in self.rate_obj:
            rt_st += str(movie) + " \n"
        return rt_st


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
        movie_id    = int(props_dict["movie id"])
        movie_title = props_dict["movie title"]
        movie_date  = props_dict["release date"]
        movie_vid   = props_dict["video release date"]
        movie_url   = props_dict["IMDb URL"]

        movie = Movie(movie_id, movie_title, movie_date,
                      movie_vid, movie_url)
        for i in range(5,len(props_dict)):
            if int(row[i]) == 1:
                movie.add_genre(row[i])
        movie_dict[int(props_dict["movie id"])] = movie

print(" ")
print(" 10 random movies ")
for i in range(10):
    tag = random.choice(list(movie_dict.keys()))
    print(str(tag).rjust(5) + " " + str(movie_dict[tag]))


user_dict = {}
with open("ml-100k/u.data") as file:
    reader = csv.reader(file, delimiter="\t")
    for row in reader:
        user_vals = [int(x) for x in row]
        user_id     = user_vals[0]
        movie_id    = user_vals[1]
        rating      = user_vals[2]
        timestamp   = user_vals[3]
        if user_id not in user_dict:
            user_dict[user_id] = User(user_id)
        user = user_dict[user_id]
        movie = movie_dict[movie_id]
        user_dict[user_id].add_rating(movie_id, movie, rating)
        movie_dict[movie_id].add_rating(user_id, user, rating)

print(" ")
print(" 10 random users")
for row in range(10):
    tag = random.choice(list(user_dict.keys()))
    print(user_dict[tag])

def print_top_10():
    print(" ")
    print(" 10 top rated movies ")
    top10 = sorted(movie_dict, key=movie_dict.get, reverse=True)[:10]
    for i in range(10):
        movie = movie_dict[top10[i]]
        print(str(movie).ljust(50)+" "+str(round(movie.avg(),2)).rjust(6))

print_top_10()

current_user_id = random.choice(list(user_dict.keys()))
current_user = user_dict[current_user_id]
exclude = True

print(" ")
print(" We will now exclude movies watched by Mr./Mrs. "+str(current_user_id))
print(str(current_user))
#print(current_user.movie_hist())
print_top_10()

def euclidean_distance(v, w):
    """Given two lists, give the Euclidean distance between them on a scale
    of 0 to 1. 1 means the two lists are identical.
    """

    # Guard against empty lists.
    if len(v) is 0:
        return 0

    # Note that this is the same as vector subtraction.
    differences = [v[idx] - w[idx] for idx in range(len(v))]
    squares = [diff ** 2 for diff in differences]
    sum_of_squares = sum(squares)

    return 1 / (1 + math.sqrt(sum_of_squares))



def pearson_product(v, w):

    if len(v) <= 1:
        return 0

    v_avg = sum(v)/len(v)
    w_avg = sum(w)/len(w)
    v_std = math.sqrt(sum((x-v_avg)**2 for x in v))
    w_std = math.sqrt(sum((y-w_avg)**2 for y in w))

    cov = sum((x-v_avg)*(y-w_avg) for x, y in zip(v, w))

    return cov/(v_std*w_std)

def common_movies(user1, user2):
    indicies = []
    u1_stars = []
    u2_stars = []
    for m1 in user1.rate_val:
        for m2 in user2.rate_val:
            if m1 == m2:
                indicies.append(m1)
                u1_stars.append(user1.rate_val[m1])
                u2_stars.append(user2.rate_val[m2])
    return u1_stars, u2_stars

u1 = current_user

print(" ")
print(" Comparing two random users")
print("  Euclidian    Pearson")

for i in range(5):

    print(" new set")

    while True:
        u2 = user_dict[random.choice(list(user_dict.keys()))]
        if u1 != u2:
            break

    u1s, u2s = common_movies(u1, u2)

    print(u1s)
    print(u2s)

    print(str(round(euclidean_distance(u1s, u2s),2)).rjust(6) +
          str(round(pearson_product(u1s, u2s),2)).rjust(6))
