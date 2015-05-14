import csv
#open the file
with open('data/u.data') as rating_data:
    rate_data = csv.reader(rating_data, delimiter='\t')
    movie_rate_data = {}
    user_data = {}
    for data in rate_data:
        if int(data[1]) in movie_rate_data:
            movie_rate_data[int(data[1])].append(int(data[2]))
        else:
            movie_rate_data[int(data[1])] = [int(data[2])]
        if int(data[0]) in user_data:
            user_data[int(data[0])].append((int(data[1]), int(data[2])))
        else:
            user_data[int(data[0])] = [(int(data[1]), int(data[2]))]

with open('data/u.item', encoding='ISO-8859-1') as movie_data:
    movie_details = csv.reader(movie_data, delimiter='|')
    movie_titles = {}
    for movie in movie_details:
        if int(movie[0]) in movie_titles:
            movie_titles[int(movie[0])].append(movie[1].split(','))
        else:
            movie_titles[int(movie[0])] = movie[1].split(',')

def movie_ratings(movie_id):
    movie_title = movie_titles[movie_id][0]
    movie_ratings = movie_rate_data[movie_id]
    return "{}\n {}".format(movie_title,movie_ratings)

print(movie_ratings(1226))

def average_rating(movie_id):
    movie_title = movie_titles[movie_id][0]
    movie_ratings = movie_rate_data[movie_id]
    average = sum(movie_ratings)/len(movie_ratings)
    return "Movie: {}:\tOverall Rating {}".format(movie_title, average)

print(average_rating(1226))

def movie_title(movie_id):
    return movie_titles[movie_id][0]

def user_ratings(user_id):
    user_ratings = user_data[user_id]
    for rate in user_ratings:
        print("Movie: {}\t Rating {}".format(movie_title(rate[0]), rate[1]))

user_ratings(27)
