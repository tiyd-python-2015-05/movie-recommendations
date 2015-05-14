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
