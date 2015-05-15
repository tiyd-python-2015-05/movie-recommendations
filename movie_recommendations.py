from movies_data import MoviesData
import sys
class MovieRecommender(MoviesData):

    def welcome(self):
        print("==========MOVIE RECOMMENDER==========")
        print("Enter the corresponding number for the service you want!")
        print("\t\t1 - To see ratings for a movie of your choice (Use Movie ID)\n \
               2 - Look at average rating for a movie of choice\n \
               3 - Check the name for the Movie ID you have\n \
               4 - See how a certain user (with USER ID) has rated several movies\n \
               5 - Want to see popular movies?\n \
               6 - Want to see top movies that a certain user (USER ID) has not seen\n \
               7 - Want to get similarities between two different users?\n \
               8 - Want a suggestion for movies to watch that you have not watched\n")

        print("At any time, press 0 (zero) to quit")

    def get_user_choice(self, servicemessage = "What service do you want? ",
                        errormessage = "You have to enter a number in the range 0 - 8"):
        try:
            userchoice = int(input(servicemessage))
            return userchoice
        except:
            print(errormessage)
            self.get_user_choice()

    def start_recommender(self,userchoice):
        if userchoice == 0:
            print("Bye")
            sys.exit()

        elif userchoice == 1:
            movieid = self.get_user_choice("Movie ID: ", "Enter a valid movie ID")
            title, ntimes,rating,avg_rate = self.movie_ratings(movieid)
            print("Title: {}\nRated: {} times\nRating: {}\nAverage Rating: {}"
                    .format(title, ntimes,rating,avg_rate))

        elif userchoice == 2:
            movieid = self.get_user_choice("Movie ID: ", "Enter a valid movie ID")
            title, ntimes,rating,avg_rate = self.movie_ratings(movieid)
            print("Title: {}\nAverage Rating: {}\nRated {} times".format(title, avg_rate, ntimes))

        elif userchoice == 3:
            movieid = self.get_user_choice("Movie ID: ", "Enter a valid movie ID")
            title, ntimes,rating,avg_rate = self.movie_ratings(movieid)
            print("Title: {}\nAverage Rating: {}".format(title, avg_rate))

        elif userchoice == 4:
            userid = self.get_user_choice("User ID: ", "Enter a valid User ID")
            user_movie_ratings = self.user_ratings(userid)
            for movie in user_movie_ratings:
                print("Movie:\t {}\n Rating: {}\n".format(self.movie_title(movie), user_movie_ratings[movie]))

        elif userchoice == 5:
            print("You can choose Popular movies based on the number of reviews")
            review_number = self.get_user_choice("How many times should movies be reviewed? : ", "Enter a valid number")
            pop_moview = self.popular_movies(review_number)
            for movieid in pop_moview:
                print("Title: {}\nAverage Rating: {}".format(self.movie_title(movieid), pop_moview[movieid]))










if __name__ == '__main__':
    movie = MovieRecommender('data/u.data', 'data/u.item')

    movie.welcome()
    choice = movie.get_user_choice()
    movie.start_recommender(choice)
