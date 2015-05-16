from functools import reduce


class Frame:
    def __init__(self, names, data):
            self.data = data
            self.names = names

    def ratings_by_id(self, movie_id):
        """
        Returns a list all ratings for a given movie
        """
        if movie_id in self.names:
            return [self.data[item] for item in self.data if item[1] == movie_id]
        else:
            return "No movies found with that ID"

    def average_by_id(self, movie_id):
        """
        calculates the average rating for a given movie
        """
        if movie_id in self.names:
            return sum(self.ratings_by_id(movie_id)) \
                / len(self.ratings_by_id(movie_id)), \
                    len(self.ratings_by_id(movie_id))
        else:
            return "No movies found with that ID"


    def name_by_id(self, movie_id):
        """
        returns the name of the movie with the given ID if it is
        in the movie list
        """
        if movie_id in self.names:
            return self.names[movie_id]

        return "No movies found with that ID"

    def top_movies(self, k=5):
        averages = list(map(self.average_by_id,
                       {row[1] for row in self.data}))

        averages = [item[0] for item in averages if item[1] >= 5]

        averages = sorted(zip(self.names, averages),
                          key=lambda x: x[1], reverse = True)

        return [self.names[entry[0]] for entry in averages[:k]]

    def movies_by_user(self, user_id):
        """
        returns dictionary with movie: rating
        by the given user
        """
        return {item[1]: self.data[item] for item
                in self.data if item[0] == user_id}

    @property
    def users(self):
        return [name for name in {name[0] for name in self.data}]

    def users_by_movie(self, movie_id):
        return {item[0]: self.data[item] for item in self.data
                if item[1] == movie_id}
