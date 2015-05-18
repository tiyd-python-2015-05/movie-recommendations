import csv
import random
import functools
import math


class RatingException(Exception):
    pass


# Global variables
exclude = False
current_user = None
use_1m = True
use_pearson = True


class MovieOrUser:

    def __init__(self):
        self.rate_val = {}

    def avg(self):
        lval = list(self.rate_val.values())

    def avg(self):
        lval = list(self.rate_val.values())
        return sum(lval) / len(lval)

    def std(self):
        lval = list(self.rate_val.values())
        mean = self.avg()
        return sum((i - mean)**2 for i in lval)**(0.5) / len(lval)

    def add_rating(self, object_id, rating):
        self.rate_val[object_id] = rating

    def avg_cutoff(self):
        lval = list(self.rate_val.values())
        if len(lval) < 5:  # few reviews, send to bottom of list
            return 0
        if exclude and self.idVal in current_user.rate_val.keys():
            return 0
        ans = sum(lval) / len(lval)
        return ans

    def __add__(self, other):
        '''Returns 3 lists of movies in common between u1 and u2
            lists are (ID, user #1 stars, user #2 stars)'''
        indicies = []
        o1_stars = []
        o2_stars = []
        for op1 in self.rate_val:
            for op2 in other.rate_val:
                if op1 == op2:
                    indicies.append(op1)
                    o1_stars.append(self.rate_val[op1])
                    o2_stars.append(other.rate_val[op2])
        return indicies, o1_stars, o2_stars

    def similar(self, the_dict):
        '''If movie, returns list about similar movies
           if user, returns list about similar users
            (id value of similar ones, correlation coefficient)
            previously called common_objects'''
        similar_ids = [0 for i in range(5)]
        similar_sc = [0 for i in range(5)]
        for o2_id in the_dict.keys():
            if o2_id != self.idVal:
                o2 = the_dict[o2_id]
                o12mid, o1s, o2s = self + o2
                if use_pearson:
                    score = pearson_product(o1s, o2s)
                else:
                    score = euclidean_distance(o1s, o2s)
                if score > min(similar_sc) and len(o1s) > 5:
                    i = similar_sc.index(min(similar_sc))
                    similar_ids[i] = o2_id
                    similar_sc[i] = score
        return similar_ids, similar_sc


@functools.total_ordering
class Movie(MovieOrUser):

    def __init__(self, idVal, title, rd, video_rd, url):
        MovieOrUser.__init__(self)
        self.idVal = idVal
        self.title = title
        self.rd = rd
        self.video_rd = video_rd
        self.url = url
        self.genre = []
        self.user_FOM = []

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.idVal == other.idVal

    def __lt__(self, other):
        if self.avg_cutoff() == other.avg_cutoff():
            return self.idVal < other.idVal
        else:
            return self.avg_cutoff() < other.avg_cutoff()

    def add_genre(self, text):
        self.genre.append(text)

    def print_genres(self):
        rt_st = ""
        for g in self.genre:
            rt_st += g + " "
        return rt_st

    def add_score(self, a_score):
        self.user_FOM.append(a_score)

    def suggest(self):
        if len(self.user_FOM) == 0:
            return 0
        else:
            return max(self.user_FOM)


class User(MovieOrUser):

    def __init__(self, idVal):
        MovieOrUser.__init__(self)
        self.idVal = idVal

    def __str__(self):
        rt_st = "reviewed " + str(len(self.rate_val)).rjust(4) + " movies, "
        rt_st += " avg score of " + str(round(self.avg(), 2)) + " stars, "
        rt_st += " std of " + str(round(self.std(), 2)) + " stars"
        return rt_st

    def movie_hist(self):
        rt_st = ""
        for movie in self.rate_obj:
            rt_st += str(movie) + " \n"
        return rt_st


# ~~~~~~ Function Definitions ~~~~~~~

def fix_row(row):
    '''csv reader will not accept multiple character delimeter
       so this is a band-aid fix to sanitize a row with corrupted
       characters'''
    store = row
    for i in range(len(store)):
        store[i].replace(":", "")
    new_row = []
    for st in store:
        if len(st) > 0:
            new_row.append(st)
    return new_row


def sanitize_input(text):
    val = input(text)
    while len(val) < 1:
        val = input(" please give a vaid selection, " + text)
    val = val[0].lower()
    return val


def read_movie_file():

    user_key = ["user id", "item id", "rating", "timestamp"]
    movie_key = ["movie id", "movie title", "release date",
                 "video release date", "IMDb URL", "unknown",
                 "Action", "Adventure", "Animation",
                 "Children's", "Comedy", "Crime", "Documentary", "Drama",
                 "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
                 "Romance", "Sci-Fi", "Thriller", "War", "Western"]

    movie_dict = {}
    file_100k = "ml-100k/u.item"
    file_1m = "ml-1m/movies.dat"
    if not use_1m:
        file_name = file_100k
        d_key = "|"
    else:
        file_name = file_1m
        d_key = ":"
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=d_key)
        for row in reader:
            props_dict = {}
            if use_1m:
                row = fix_row(row)
                movie_id = int(row[0])
                movie_title = row[1]
                movie_date = ""
                movie_vid = ""
                movie_url = ""
            else:
                for i in range(len(movie_key)):
                    props_dict[movie_key[i]] = row[i]
                movie_id = int(props_dict["movie id"])
                movie_title = props_dict["movie title"]
                movie_date = props_dict["release date"]
                movie_vid = props_dict["video release date"]
                movie_url = props_dict["IMDb URL"]

            movie = Movie(movie_id, movie_title, movie_date,
                          movie_vid, movie_url)
            if use_1m:
                for i in range(2, len(row)):
                    movie.add_genre(row[i])
            else:
                for i in range(5, len(props_dict)):
                    if int(row[i]) == 1:
                        movie.add_genre(movie_key[i])
            movie_dict[movie_id] = movie

    return movie_dict


def read_user_file():
    user_dict = {}

    file_100k = "ml-100k/u.data"
    file_1m = "ml-1m/ratings.dat"
    if not use_1m:
        file_name = file_100k
        d_key = "\t"
    else:
        file_name = file_1m
        d_key = ":"
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=d_key)
        for row in reader:
            if use_1m:
                row = fix_row(row)
            user_vals = [int(x) for x in row]
            user_id = user_vals[0]
            movie_id = user_vals[1]
            rating = user_vals[2]
            timestamp = user_vals[3]
            if user_id not in user_dict:
                user_dict[user_id] = User(user_id)
            user = user_dict[user_id]
            movie = movie_dict[movie_id]
            user_dict[user_id].add_rating(movie_id, rating)
            movie_dict[movie_id].add_rating(user_id, rating)

    return user_dict


def search_for_movie(movie_dict):
    print(" ")
    text = input(" type string to search for:  ")
    while True:
        movie_ids = []
        for tag in movie_dict.keys():
            if text.lower() in (movie_dict[tag].title).lower():
                movie_ids.append(tag)
        i_max = 10
        if len(movie_ids) < 10:
            i_max = len(movie_ids)
        for i in range(i_max):
            print(str(i + 1) + " " + str(movie_dict[movie_ids[i]]))
        print(" ")
        text = input(" make a selection or type a new search: ")
        if len(text) == 0:
            text = " "
        if text[0].isdigit():
            break
    return movie_ids[i - 1]
    print(" ")


# Printing Functions
def print_top_10_movies(movie_dict):
    print(" ")
    print(" 10 top rated movies ")
    top10 = sorted(movie_dict, key=movie_dict.get, reverse=True)[:10]
    for i in range(10):
        movie = movie_dict[top10[i]]
        print(str(movie).ljust(50) + " " + str(round(movie.avg(), 2)).rjust(6))


def print_random_10_movies(movie_dict):
    print(" ")
    print(" 10 random movies ")
    for i in range(10):
        tag = random.choice(list(movie_dict.keys()))
        print(str(tag).rjust(5) + " " + str(movie_dict[tag]))
        print("     " + movie_dict[tag].print_genres())


def print_random_10_users(user_dict):
    print(" ")
    print(" 10 random users")
    for row in range(10):
        tag = random.choice(list(user_dict.keys()))
        print(user_dict[tag])


def print_top_10_exclude(movie_dict):
    print(" ")
    print(" We will now exclude movies watched by Mr./Mrs. " +
          str(current_user_id))
    print(str(current_user))

    print_top_10_movies(movie_dict)


def compare_random_users(user_dict):
    print(" ")
    print(" Comparing two random users")
    print("  Euclidian    Pearson")

    u1 = current_user

    for i in range(5):

        while True:
            u2 = user_dict[random.choice(list(user_dict.keys()))]
            if u1 != u2:
                break
        u12mid, u1s, u2s = u1 + u2

        print("user1: " + " ".join([str(u1s[i]) for i in range(len(u1s))]))
        print("user2: " + " ".join([str(u2s[i]) for i in range(len(u2s))]))
        print("correlation level: " +
              str(round(euclidean_distance(u1s, u2s), 2)).rjust(6) +
              str(round(pearson_product(u1s, u2s), 2)).rjust(6))


def similarity_suggestions(movie_dict, user_dict):

    print(" ")
    print(" Top movies out of your history")
    print("                                  Title              Score")

    u1 = current_user
    personal_best = u1.rate_val
    personal_best = sorted(personal_best, key=personal_best.get,
                           reverse=True)

    i_max = 5
    if len(personal_best) < 5:
        i_max = len(personal_best)
    for i in range(i_max):
        print(str(movie_dict[personal_best[i]]).rjust(50) + " " +
              str(u1.rate_val[personal_best[i]]).rjust(6))

    print(" ")
    print(" Watch reccomendations based off similar users")
    print("                                   Title             Score")
    group_ids, group_scores = current_user.similar(user_dict)

    for i in range(len(group_ids)):
        u2 = user_dict[group_ids[i]]
        for m_id in u2.rate_val.keys():
            if m_id not in u1.rate_val.keys():
                the_score = group_scores[i] * u2.rate_val[m_id]
                movie_dict[m_id].add_score(the_score)

    top_scores = [0 for i in range(10)]
    top_mid = [0 for i in range(10)]
    for m_id in movie_dict:
        the_score = movie_dict[m_id].suggest()
        if the_score > min(top_scores):
            i = top_scores.index(min(top_scores))
            top_scores[i] = the_score
            top_mid[i] = m_id

    i_max = 10
    for i in range(10):
        if top_mid[i] != 0:
            print(str(movie_dict[top_mid[i]]).rjust(50) + " " +
                  str(round(top_scores[i], 2)))


def similar_movie_suggest(m_id, movie_dict, user_dict):
    print(" ")
    current_movie = movie_dict[m_id]
    print(" Movies similar to '" + str(current_movie) + "'")
    print("based on user score correlation")
    print(" ")
    ids, scores = current_movie.similar(movie_dict)
    for i in range(len(ids)):
        if ids[i] != 0:
            print(str(i) + " " + str(movie_dict[ids[i]]))
    print(" ")
    print(" Pick a movie to switch to, or just hit enter")
    sel = input("   enter selection: ")
    if len(sel) > 0:
        return ids[int(sel)]
    else:
        return m_id


# Math Functions


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

    v_avg = sum(v) / len(v)
    w_avg = sum(w) / len(w)
    v_std = math.sqrt(sum((x - v_avg)**2 for x in v))
    w_std = math.sqrt(sum((y - w_avg)**2 for y in w))

    cov = sum((x - v_avg) * (y - w_avg) for x, y in zip(v, w))

    if v_std > 0 and w_std > 0:
        return cov / (v_std * w_std)
    else:
        return 0


if __name__ == '__main__':

    # File Reading
    print(" ")
    sel = sanitize_input("Use database with 1 [M]illion or" +
                         " 100 [T]housand ratings: ")
    if sel == "M":
        use_1m = True
    else:
        use_1m = False
    movie_dict = read_movie_file()

    # Read user data
    user_dict = read_user_file()

    # Pick current user
    while True:
        current_user_id = random.choice(list(user_dict.keys()))
        current_user = user_dict[current_user_id]
        if len(current_user.rate_val) >= 5:  # must have reviewed several
            break
    exclude = True
    # Pick current movie
    current_movie_id = random.choice(list(movie_dict.keys()))
    current_movie = movie_dict[current_movie_id]

    while True:

        print(" ")
        print(" ")
        print("Data is loaded. What do you want to do with it?")
        print(" current user is #" + str(current_user_id))
        print(" current movie is '" + str(current_movie) + "'")
        if use_pearson:
            cor_text = "pearson correlation"
        else:
            cor_text = "euclidian distance"
        print(" using similarity distance of " + cor_text)
        print("  1: print 10 random movies")
        print("  2: select user account by ID")
        print("  3: view comparision to 5 random users")
        print("  4: print top 10 overall movies")
        print("  5: print top 10 overall movies unwatched by user")
        print("  6: print 10 random users")
        print("  7: view suggestions based on similar users")
        print("  8: change the type of similarity distance calc")
        print("  9: change current movie by searching")
        print("  0: suggest similar movies to current one")
        print("  e: exit")
        print(" ")

        val = sanitize_input(" enter selection: ")

        if val == "1":
            # Demonstrate database - print 10 random movies with genres
            print_random_10_movies(movie_dict)
        elif val == "2":
            uid = int(input("\n enter user ID: "))
            current_user_id = uid
            current_user = user_dict[current_user_id]
        elif val == "3":
            compare_random_users(user_dict)
        elif val == "4":
            exclude = False
            print_top_10_movies(movie_dict)
            exclude = True
        elif val == "5":
            print_top_10_exclude(movie_dict)
        elif val == "6":
            print_random_10_users(user_dict)
        elif val == "7":
            similarity_suggestions(movie_dict, user_dict)
        elif val == "8":
            if use_pearson:
                use_pearson = False
            else:
                use_pearson = True
        elif val == "9":
            current_movie_id = search_for_movie(movie_dict)
            current_movie = movie_dict[current_movie_id]
        elif val == "0":
            current_movie_id = similar_movie_suggest(
                current_movie_id, movie_dict, user_dict)
            current_movie = movie_dict[current_movie_id]
        elif val == "e":
            break

    print(" ")
