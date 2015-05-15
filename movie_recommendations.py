from data_handling import *
import math

movie_data = get_movie_data("movie_lens-100k/u.item")
user_data = get_user_data("movie_lens-100k/u.data")

user_mov_rating = get_user_mov_rating(user_data)
user_movs = get_user_movs(user_data)
mov_ratings = get_movie_ratings(user_data)

def find_all_ratings_for_movie(movie):
	return mov_ratings[movie]

def average_rating(movie,min_ratings=5):
	all_ratings = find_all_ratings_for_movie(movie)
	if len(all_ratings) < min_ratings:
		return None
	else:
		average = sum(all_ratings)/len(all_ratings)
		return average

def get_movie_name(movie):
    return str(movie_data[movie])

def find_all_ratings_for_user(user):
    return [tup[1] for tup in user_mov_rating[user]]

def return_top_movies(n, min_ratings=5):
	averages = {}
	for item in movie_data.items():
		avg = average_rating(item[0], min_ratings)
		if avg != None:
			averages[item[1].title] = avg
	sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)
	top = sorted_avgs[0:n]
	return [t[0] for t in top]

def top_movies_for_user(user, n, min_ratings=5):
	averages = {}
	for item in movie_data.items():
		avg = average_rating(item[0], min_ratings)
		if avg != None and item[0] not in user_movs[user]:
			averages[item[1].title] = avg
	sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)
	top = sorted_avgs[0:n]
	return [t[0] for t in top]

def common_movies(user1, user2):
	movies_in_common = []
	user1_movies = user_movs[user1]
	user2_movies = user_movs[user2]
	for movie in user1_movies:
		if movie in user2_movies:
			movies_in_common.append(movie)
	return (movies_in_common)

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

def get_euclidean_distance(user1,user2):
    com_mov = sorted(common_movies(user1,user2))
    user1_ratings = []
    user2_ratings = []
    if len(com_mov) < 4:
        return 0
    else:
        for movie in com_mov:
            for pair in user_mov_rating[user1]:
                if movie == pair[0]:
                    user1_ratings.append(pair[1])
        for movie in com_mov:
            for pair in user_mov_rating[user2]:
                if movie == pair[0]:
                    user2_ratings.append(pair[1])
    return euclidean_distance(user1_ratings, user2_ratings)

def find_ten_most_similar_users(user, n):
	similarities = {}
	top = []
	for other_user in [user[0] for user in user_movs.items()]:
		if other_user != user:
			sim = get_euclidean_distance(user,other_user)
			similarities[other_user] = sim
	sorted_sims = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
	top = sorted_sims[0:n]
	return top

def recommend_movies_from_sim_users(user, n):
    top = find_ten_most_similar_users(user, n)
    recommendations = []
    comp_list = []
    comp_dict = {}
    for pair in top:
        max_rating = 0
        for mov_rate in user_mov_rating[pair[0]]:
            if mov_rate[1] > max_rating and mov_rate[0] not in user_movs[user]:
                max_rating = mov_rate[1]
                sim_mov_rate = (pair[1],mov_rate[0],mov_rate[1])
        comp_list.append(sim_mov_rate)
    for tup in comp_list:
        compatability = tup[0] * tup[2]
        comp_dict[movie_data[tup[1]]] = compatability
    top_movies = sorted(comp_dict.items(), key=lambda x: x[1], reverse=True)
    return [t[0] for t in top_movies]
