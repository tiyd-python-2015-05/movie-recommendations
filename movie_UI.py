from movie_recommendations import *

if __name__ == '__main__':
	print("Hello, what movie lists are you interested in seeing?")
	choice = input("1. Top movies based on 100,000 user ratings\n"
				   "2. Popular movies that you haven't seen\n"
				   "3. Movies recommended for you based on similar users\n"
				   "Choose 1, 2, or 3: ")
	if choice == '1':
		n = input("How many movies do you want in the list? ")
		r = input("What is the minimum number of ratings a movie must have? ")
		top_movs = return_top_movies(int(n), int(r))
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))

	if choice == '2':
		usr_id = input("What is your user ID? ")
		n = input("How many movies do you want in the list? ")
		r = input("What is the minimum number of ratings a movie must have? ")
		top_movs = top_movies_for_user(int(usr_id),int(n), int(r))
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))

	if choice == '3':
		usr_id = input("What is your user ID? ")
		n = input("How many movies do you want in the list? ")
		top_movs = recommend_movies_from_sim_users(int(usr_id), int(n))
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
