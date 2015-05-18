import csv


class Movie:
    movie_titles = {}
    movie_rat_id = {}
    user_ratings = {}
    avg_movie_rat = {}

    def __init__(self):
        with open("ml-100k/u.item", encoding='windows-1252') as file:
            reader = csv.reader(file, delimiter = "|")
            for row in reader:
                self.movie_titles[int(row[0])] = row[1]

        with open("ml-100k/u.data", encoding='windows-1252') as file:
            reader = csv.reader(file, delimiter = "\t")
            for row in reader:
                if (int(row[0])) not in self.user_ratings:
                    self.user_ratings[(int(row[0]))] = {(int(row[1])): (int(row[2]))}
                else:
                    self.user_ratings[(int(row[0]))].update({(int(row[1])): (int(row[2]))})

                if (int(row[1])) not in self.movie_rat_id:
                    self.movie_rat_id[(int(row[1]))] = [int(row[2])]
                else:
                    self.movie_rat_id[(int(row[1]))].append(int(row[2]))

        for k, v in self.movie_rat_id.items():
            self.avg_movie_rat[k] = self.avg_rating_by_id(k)



    def movie_by_id(self, mid):
        if mid in self.movie_titles:
            return self.movie_titles[mid]
        else:
            return "No movie exist by that id"


    def movie_rat_by_id(self, mid):
        if mid in self.movie_rat_id:
            return self.movie_rat_id[mid]
        else:
            return "No movie exist by that id"


    def avg_rating_by_id(self, mid):
        ratings = self.movie_rat_by_id(mid)
        return sum(ratings) / len(ratings)


    def ratings_by_uid(self, uid):
        ratings_by_user = []
        ratings = self.user_ratings[uid]
        for k, v in ratings.items():
            ratings_by_user.append(v)
        return ratings_by_user

    def top_20_movies(self):
        top_20_movies = sorted(self.avg_movie_rat.items(),
                                     key=lambda x: x[1], reverse=True)[:20]
        return top_20_movies



class Start:
    def menu(self):
        print("Enter [1] to get the title of a movie by movie id.")
        print("Enter [2] to get all the ratings by movie id.")
        print("Enter [3] to get average rating of a movie by movie id.")
        print("Enter [4] to get all the ratings by a user.")
        print("Enter [5] to get top 20 movies by average user rating.")
        user_input = int(input("Choose one of the above. What would you like to do? "))

        return user_input

    def get_mid(self):
        mid = int(input("Enter a movie id: "))
        return mid


    def get_uid(self):
        uid = int(input("Enter user id: "))
        return uid

    def recommend(self, user_input):
        movie = Movie()
        if user_input == 1:
            mid = self.get_mid()
            return movie.movie_by_id(mid)
        elif user_input == 2:
            mid = self.get_mid()
            return movie.movie_rat_by_id(mid)
        elif user_input == 3:
            mid = self.get_mid()
            return movie.avg_rating_by_id(mid)
        elif user_input == 4:
            uid = self.get_uid()
            return movie.ratings_by_uid(uid)
        elif user_input == 5:
            top = movie.top_20_movies()
            for k, v in top:
                print (k, movie.movie_by_id(k))

if __name__ == "__main__":
    start = Start()
    user_input = start.menu()
    print(start.recommend(user_input))
