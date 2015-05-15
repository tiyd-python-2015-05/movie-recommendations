import csv


info_list = ['id', 'title', 'released', 'on_video', 'url', 'unknown',
             'Action', 'Adventure', 'Animation', 'Children', 'Comedy',
             'Crime', 'Documentary', 'Drama', 'Fantasy', 'Noir', 'Horror',
             'Musical', 'Mystery', 'Romance', 'Scifi', 'Thriller', 'War',
             'Western']

data_list = ["User", "mov_id", "rating", "timestamp"]

def load():
    movie_titles = {}
    data = {}
    with open('./data/u.item','r', encoding='latin-1') as item_file:
        movies = csv.reader(item_file, delimiter = '|')
        for item in movies:
            movie_titles[int(item[0])] = item[1]

    with open('./data/u.data', 'r') as data_file:
        ratings = csv.reader(data_file, delimiter = '\t')
        for item in ratings:
            item = list(map(int, item))
            data[(item[0], item[1])] = item[2]


    return movie_titles, data
