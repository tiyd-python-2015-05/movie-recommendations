import csv

def get_movie_data(data_path):
    the_data = []
    with open(data_path) as file:
    	reader = csv.reader(file, delimiter = "|")
    	for row in reader:
    		the_data.append(row)
    movie_data = {int(row[0]):Movie(row[1],row[5:]) for row in the_data}
    return movie_data

def get_user_data(data_path):
    user_data = []
    with open(data_path) as file:
    	reader = csv.reader(file, delimiter = "\t")
    	for row in reader:
    		user_data.append(row)
    return user_data

def get_user_info(data_path):
    user_info = {}
    with open(data_path) as file:
    	reader = csv.reader(file, delimiter = "|")
    	for row in reader:
    		user_info[int(row[0])] = int(row[1])
    return user_info

def get_user_mov_rating(user_data):
    user_mov_rat = {}
    for user in user_data:
        if int(user[0]) not in user_mov_rat:
            user_mov_rat[int(user[0])] = [(int(user[1]),int(user[2]))]
        else:
            user_mov_rat[int(user[0])].append((int(user[1]),int(user[2])))
    return user_mov_rat

def get_user_movs(user_data):
    user_movs = {}
    for user in user_data:
        if int(user[0]) not in user_movs:
            user_movs[int(user[0])] = [int(user[1])]
        else:
            user_movs[int(user[0])].append(int(user[1]))
    return user_movs

def get_movie_ratings(user_data):
    mov_ratings = {}
    for movie in user_data:
        if int(movie[1]) not in mov_ratings:
            mov_ratings[int(movie[1])] = [int(movie[2])]
        else:
            mov_ratings[int(movie[1])].append(int(movie[2]))
    return mov_ratings

class Movie:
    def __init__(self,title,genres):
        self.title = title
        self.genre_list = genres
        self.genres = self.find_genres()

    def find_genres(self):
        return [i for i in range(19) if self.genre_list[i] == '1']

    def __repr__(self):
        return self.title
