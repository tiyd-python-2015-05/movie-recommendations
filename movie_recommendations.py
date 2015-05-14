import csv
#open the file
with open('data/u.data') as rating_data:
    rate_data = csv.reader(rating_data, delimiter='\t')
    movie_rate_data = {}
    user_data = {}
    for data in rate_data:
        if data[1] in movie_rate_data:
            movie_rate_data[data[1]].append(data[2])
        else:
            movie_rate_data[data[1]] = list(data[2])
        if data[0] in user_data:
            user_data[data[0]].append((data[1], data[2]))
        else:
            user_data[data[0]] = list( (data[1], data[2]) )

with open('data/u.item', encoding='ISO-8859-1') as movie_data:
    movie_details = csv.reader(movie_data, delimiter='|')
    movie_titles = {}
    for movie in movie_details:
        if movie[0] in movie_titles:
            movie_titles[movie[0]].append(movie[1].split(','))
        else:
            movie_titles[movie[0]] = movie[1].split(',')
