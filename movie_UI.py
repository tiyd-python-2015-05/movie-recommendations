from movie_recommendations import *

def ask_again():
	a = input("\nWould you like to see another list (Y/N)? ").lower()
	if a == 'y':
		return UI(usr_id)
	elif a == 'n':
		quit()
	else:
		print("Not a valid choice, enter Y for yes or N for no")
		return ask_again()

def UI(usr):
	usr_id = usr
	choice = input("\n1. Top movies based on 100,000 user ratings\n"
				"2. Popular movies that you haven't seen\n"
				"3. Movies recommended for you based on similar users\n"
				"4. Movies similar to a movie you enjoyed\n"
				"5. Movie recommendations within a particular genre\n"
				"6. Movies that users near you enjoyed\n"
				"\nChoose 1, 2, 3, 4, 5, or 6: ")
	if choice == '1':
		n = int(input("\nHow many movies do you want in the list? "))
		r = int(input("\nWhat is the minimum number of ratings a movie must have? "))
		if r > 40:
			print("Not enough movies have {} ratings".format(r))
			return UI(usr_id)
		top_movs = return_top_movies(n, r)
		print("\n")
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
		return ask_again()

	elif choice == '2':
		n = int(input("\nHow many movies do you want in the list? "))
		r = int(input("\nWhat is the minimum number of ratings a movie must have? "))
		if r > 40:
			print("Not enough movies have {} ratings".format(r))
			return UI(usr_id)
		top_movs = top_movies_for_user(usr_id,n,r)
		print("\n")
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
		return ask_again()

	elif choice == '3':
		n = int(input("\nHow many movies do you want in the list? "))
		top_movs = recommend_movies_from_sim_users(usr_id, n)
		print("\nUsers similar to you enjoyed:\n")
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
		return ask_again()

	elif choice == '4':
		mov_id = int(input("\nWhat's the ID of a movie you enjoyed? "))
		n = int(input("\nHow many movies do you want in the list? "))
		top_movs = recommend_sim_movies_from_ratings(mov_id,usr_id,n)
		print("\nHere are some movies similar to \"{}\":\n".format(movie_data[mov_id]))
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
		return ask_again()

	elif choice == '5':
		genre = int(input("\nWhich genre do you want to look at?\n"
					  "1. Unknown\n"
					  "2. Action\n"
					  "3. Adventure\n"
					  "4. Animation\n"
					  "5. Children's\n"
					  "6. Comedy\n"
					  "7. Crime\n"
					  "8. Documentary\n"
					  "9. Drama\n"
					  "10. Fantasy\n"
					  "11. Film-Noir\n"
					  "12. Horror\n"
					  "13. Musical\n"
					  "14. Mystery\n"
					  "15. Romance\n"
					  "16. Sci-Fi\n"
					  "17. Thriller\n"
					  "18. War\n"
					  "19. Western\n"
					  "Enter the number corresponding to your choice: "))
		n = int(input("\nHow many movies do you want in the list? "))
		r = int(input("\nWhat is the minimum number of ratings a movie must have? "))
		if r > 30:
			print("Not enough movies have {} ratings".format(r))
			return UI(usr_id)
		top_movs = recommend_movie_in_genre(genre-1, usr_id,n,r)
		print("\nHere are the top rated movies in that genre:\n")
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
		return ask_again()

	elif choice == '6':
		n = int(input("\nHow many movies do you want in the list? "))
		r = int(input("\nWhat is the minimum number of ratings a movie must have? "))
		if r > 30:
			print("Not enough movies have {} ratings".format(r))
			return UI(usr_id)
		top_movs = recommend_movies_usrs_your_age_liked(usr_id, n, r)
		print("\nHere are the top rated movies for people your age:\n")
		for i in range(len(top_movs)):
			print("{}. {}".format(i+1,top_movs[i]))
		return ask_again()

	else:
		print("Not a valid option")
		return UI()

if __name__ == '__main__':
	usr_id = int(input("Hello, what is your user ID? "))
	print("\nWhat movie lists are you interested in seeing?")
	UI(usr_id)
