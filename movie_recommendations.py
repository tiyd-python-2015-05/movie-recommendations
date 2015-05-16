from data_handling import *
import math

movie_data = get_movie_data("movie_lens-100k/u.item")
user_data = get_user_data("movie_lens-100k/u.data")
user_info = get_user_info("movie_lens-100k/u.user")

user_mov_rating = get_user_mov_rating(user_data)
user_movs = get_user_movs(user_data)
mov_ratings = get_movie_ratings(user_data)

def find_all_ratings_for_movie(movie):
	'''Returns all of the ratings for a particular movie'''
	return mov_ratings[movie]

def average_rating(movie,min_ratings=7):
	'''Returns the average rating for a particular movie'''
	all_ratings = find_all_ratings_for_movie(movie)
	if len(all_ratings) < min_ratings:
		return None
	else:
		average = sum(all_ratings)/len(all_ratings)
		return average

def find_all_ratings_for_user(user):
	'''Returns all of the ratings for a particular user'''
    return [tup[1] for tup in user_mov_rating[user]]

def return_top_movies(n, min_ratings=7):
	'''Returns the top n movies based on their average ratings'''
	averages = {}
	for item in movie_data.items():
		avg = average_rating(item[0], min_ratings)
		if avg != None:
			averages[item[1].title] = avg
	sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)
	top = sorted_avgs[0:n]
	return [t[0] for t in top]

def top_movies_for_user(user, n, min_ratings=7):
	'''Returns the top movies that a particular user hasn't seen'''
	averages = {}
	for item in movie_data.items():
		avg = average_rating(item[0], min_ratings)
		if avg != None and item[0] not in user_movs[user]:
			averages[item[1].title] = avg
	sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)
	top = sorted_avgs[0:n]
	return [t[0] for t in top]

def common_movies(user1, user2):
	'''Returns a list of movies that user1 and user2 have both seen'''
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
	'''Finds the euclidean distance(similarity) between two user's ratings'''
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

def find_most_similar_users(user, n):
	'''Returns a list of users that are most similar to the given user as determined by their
	euclidean distance'''
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
	'''Returns a list of recommended movies for a user based on users similar to them'''
    top = find_most_similar_users(user, n)
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

def find_users_who_rated_movie_high(movie):
	'''Returns a list of users who rated a particular movie highly'''
	usrs_liked_movie = []
	for user in user_mov_rating.items():
		for mov_rat_tup in user[1]:
			if mov_rat_tup[0] == movie and mov_rat_tup[1] >= 4:
				usrs_liked_movie.append(user[0])
	return usrs_liked_movie

def recommend_sim_movies_from_ratings(movie, user_id, n):
	'''Returns a list of movie recommendations when given a movie that a user particularly
	enjoyed'''
	rec_movies = []
	rec_list = []
	usrs_who_liked_movie = find_users_who_rated_movie_high(movie)
	for user in usrs_who_liked_movie:
		for movie_rat in user_mov_rating[user]:
			if movie_rat[1] >= 4 and movie_rat[0] not in user_movs[user_id]:
				rec_movies.append(movie_rat[0])
	for mov in rec_movies:
		for genre in movie_data[mov].genres:
			if genre in movie_data[movie].genres:
				rec_list.append(movie_data[mov].title)
				break
	return rec_list[0:n]

def recommend_movie_in_genre(genre, user, n, min_ratings=7):
	'''Returns a list of highly rated movies in a particular genre'''
	averages = {}
	for item in movie_data.items():
		avg = average_rating(item[0], min_ratings)
		if avg != None and genre in item[1].genres:
			averages[item[1].title] = avg
	sorted_avgs = sorted(averages.items(), key=lambda x: x[1], reverse=True)
	top = sorted_avgs[0:n]
	return [t[0] for t in top]

def recommend_movies_usrs_your_age_liked(user, n, min_ratings=7):
	'''Returns a list of movies that users within 5 years of the current users age enjoyed'''
	user_age = user_info[user]
	max_age = user_age + 5
	min_age = user_age - 5
	comp_list = []
	poss_users = []

	for pair in user_info.items():
		if min_age < pair[1] < max_age:
			poss_users.append(pair[0])
	print(poss_users)

	for usr in poss_users:
		for mov_rate in user_mov_rating[usr]:
			if mov_rate[1] >= 4 and mov_rate[0] not in user_movs[user]:
				mov = mov_rate[0]
				comp_list.append(mov)
	return [movie_data[l].title for l in comp_list][0:n]
