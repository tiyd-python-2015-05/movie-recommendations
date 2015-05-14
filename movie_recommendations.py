import csv
import math
#open the file

class MoviesData:

    movie_rate_data = {}
    user_rate_data = {}
    movie_titles = {}
    user_movies = {}
    def __init__(self, rate_data_source, movie_data_source):
        # 'data/u.data'
        with open(rate_data_source) as rating_data:
            rate_data = csv.reader(rating_data, delimiter='\t')
            for data in rate_data:
                if int(data[1]) in self.movie_rate_data:
                    self.movie_rate_data[int(data[1])].append(int(data[2]))
                else:
                    self.movie_rate_data[int(data[1])] = [int(data[2])]

                if int(data[0]) in self.user_rate_data:
                    self.user_rate_data[int(data[0])].update({int(data[1]):int(data[2])})
                    self.user_movies[int(data[0])].append(int(data[1]))
                else:
                    self.user_rate_data[int(data[0])] = {int(data[1]):int(data[2])}
                    self.user_movies[int(data[0])] = [int(data[1])]

        # 'data/u.item'
        with open(movie_data_source, encoding='ISO-8859-1') as movie_data:
            movie_details = csv.reader(movie_data, delimiter='|')
            for movie in movie_details:
                if int(movie[0]) in self.movie_titles:
                    self.movie_titles[int(movie[0])].append(movie[1].split(','))
                else:
                    self.movie_titles[int(movie[0])] = movie[1].split(',')

    # get ratings for a movie by id
    def movie_ratings(self, movie_id):
        movie_title = self.movie_titles[movie_id][0]
        movie_ratings = self.movie_rate_data[movie_id]
        return "{}\n {}".format(movie_title,movie_ratings)

    #get an average rating for a movie. to one decimal place
    def average_rating(self, movie_id):
        movie_title = self.movie_titles[movie_id][0]
        movie_ratings = self.movie_rate_data[movie_id]
        average = round(sum(movie_ratings)/len(movie_ratings),1)
        return "Movie:\t {}:\nOverall Rating: {}".format(movie_title, average)


    # get movie title
    def movie_title(self, movie_id):
        return self.movie_titles[movie_id][0]

    # get ratings a specific user has made
    def user_ratings(self, user_id):
        user_ratings = self.user_rate_data[user_id]
        for rate in user_ratings:
            print("Movie:\t {}\n Rating: {}\n".format(self.movie_title(rate[0]), rate[1]))

    def popular_movies(self):
        '''Movies rated more than 20 times'''
        popular_movies = {}
        for movie in self.movie_rate_data:
            if len(self.movie_rate_data[movie]) >= 100:
                popular_movies[movie] = round(sum(self.movie_rate_data[movie])/len(self.movie_rate_data[movie]), 1)

        return popular_movies

    def popular_movies_not_rated_by_person(self, user_id):
        '''Movies not rated by person'''
        not_rated_by = []
        for movie in self.popular_movies():
            if movie not in self.user_movies[user_id]:
                not_rated_by.append(self.movie_title(movie).split(','))
            else:
                pass
        if len(not_rated_by) == 0:
            return None
        else:
            return not_rated_by

    def ratings_for_movies_watched_by_two(self, first_user_id, second_user_id):
        user1 = []
        user2 = []
        for movie in self.user_rate_data[first_user_id]:
            if movie in self.user_rate_data[second_user_id]:
                # print("Movie {}:\n User {} rated {}: User {} rated {}".
                #         format(movie, first_user_id,self.user_rate_data[first_user_id][movie],
                #                 second_user_id,self.user_rate_data[second_user_id][movie]))
                user1.append(self.user_rate_data[first_user_id][movie])
                user2.append(self.user_rate_data[second_user_id][movie])
        return user1, user2


    def euclidean_distance(self,v, w):
        """Given two lists, give the Euclidean distance between them on a scale
        of 0 to 1. 1 means the two lists are identical.
        """
        # Guard against empty lists.
        if len(v) is 0:
            return 0

        differences = [v[idx] - w[idx] for idx in range(len(v))]
        squares = [diff ** 2 for diff in differences]
        sum_of_squares = sum(squares)

        return round(1 / (1 + math.sqrt(sum_of_squares)), 1)



if __name__ == '__main__':
    movie = MoviesData('data/u.data', 'data/u.item')

    #print(movie.movie_ratings(1227))
    #print(movie.average_rating(727))
    #movie.user_ratings(23)
    #print(movie.movie_title(727))

    #print(movie.user_movies)
    rates = movie.ratings_for_movies_watched_by_two(1,2)
    print(rates)
    print(movie.euclidean_distance(rates[0], rates[1]))
#    print(movie.user_rate_data[2])
    #print(movie.popular_movies_not_rated_by_person(27))
    if movie.popular_movies_not_rated_by_person(27) != None:
        for kamuvi in movie.popular_movies_not_rated_by_person(27):
            #print(kamuvi[0])
            pass
