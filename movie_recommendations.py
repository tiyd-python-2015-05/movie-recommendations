import csv
#open the file

class MoviesData:

    movie_rate_data = {}
    user_data = {}
    movie_titles = {}
    def __init__(self, rate_data_source, movie_data_source):
        # 'data/u.data'
        with open(rate_data_source) as rating_data:
            rate_data = csv.reader(rating_data, delimiter='\t')
            for data in rate_data:
                if int(data[1]) in self.movie_rate_data:
                    self.movie_rate_data[int(data[1])].append(int(data[2]))
                else:
                    self.movie_rate_data[int(data[1])] = [int(data[2])]
                if int(data[0]) in self.user_data:
                    self.user_data[int(data[0])].append((int(data[1]), int(data[2])))
                else:
                    self.user_data[int(data[0])] = [(int(data[1]), int(data[2]))]

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
        average = sum(movie_ratings)/len(movie_ratings)
        return "Movie:\t {}:\nOverall Rating: {}".format(movie_title, average)


    # get movie title
    def movie_title(self, movie_id):
        return self.movie_titles[movie_id][0]

    # get ratings a specific user has made
    def user_ratings(self, user_id):
        user_ratings = self.user_data[user_id]
        for rate in user_ratings:
            print("Movie:\t {}\n Rating: {}\n".format(self.movie_title(rate[0]), rate[1]))

    # get top movies

movie = MoviesData('data/u.data', 'data/u.item')

print(movie.movie_ratings(1227))
print(movie.average_rating(727))
movie.user_ratings(23)
print(movie.movie_title(727))
