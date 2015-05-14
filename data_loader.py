import csv


# u.info
"""
movie id | movie title | release date | video release date |
IMDb URL | unknown | Action | Adventure | Animation |
Children's | Comedy | Crime | Documentary | Drama | Fantasy |
Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
Thriller | War | Western |
"""

# u.user
"""
Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.
"""

def load_data(filename="datasets/ml-100k/u.data"):
    # u.data
    # user id | item id | rating | timestamp
    fieldnames = ['user_id','item_id','rating','timestamp']
    with open(filename) as file:
        reader = csv.DictReader(file, delimiter='\t', fieldnames=fieldnames)
        ratings = Ratings()
        for row in reader:
            ratings.add_rating(**row)
        return ratings

class Ratings():
    def __init__(self):
        self._ratings = {}
        # self._flat_ratings = {}
    def add_rating(self, user_id, item_id, rating, timestamp):
        current_ratings = self._ratings.setdefault(item_id,[])
        current_ratings.append([{'user_id': user_id,
                                 'rating': rating,
                                 'timestamp': timestamp
                                }])
        self._ratings[item_id] = current_ratings

    def show_item_ratings(self, item_id):
        num_ratings = len(self._ratings[item_id])
        print('Showing {} ratings for Item {}'.format(num_ratings, item_id))
        fieldnames = ['user_id','rating','timestamp']
        for item in fieldnames:
            print(item, ' ', end='')
        print('\n==========================')
        for i in self._ratings[item_id]:
            print('{user_id}\t   {rating}\t {timestamp}'.format(**i[0]))
        # print(users._users['196'])

if __name__ == '__main__':
    users = load_data()
    users.show_item_ratings('192')
