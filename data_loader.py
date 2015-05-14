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
        #headers = next(reader)
        headers = fieldnames
        print(headers)
        print("---")
        # line = next(reader)
        # print(line)
        users = Users()
        for row in reader:
            users.add_rating(**row)
        return users

class Users():
    def __init__(self):
        self._users = {}
    def add_rating(self, user_id, item_id, rating, timestamp):
        current_ratings = self._users.setdefault(user_id,[])
        current_ratings.append([{'item_id': item_id,
                                 'rating': rating,
                                 'timestamp': timestamp
                                }])
        self._users[user_id] = current_ratings
    def show_user_ratings(self, user_id):
        num_ratings = len(users._users[user_id])
        print('Showing {} ratings for User {}'.format(num_ratings, user_id))
        fieldnames = ['item_id','rating','timestamp']
        for item in fieldnames:
            print(item, ' ', end='')
        print('\n==========================')
        for i in users._users[user_id]:
            print('{item_id}\t   {rating}\t {timestamp}'.format(**i[0]))
        # print(users._users['196'])

if __name__ == '__main__':
    users = load_data()
    users.show_user_ratings('192')
