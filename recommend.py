import csv
import pprint

users = {}
movies = {}
ratings = {}

class User():
    def __init__(self, user_id='1', age='24', gender='M', job='technician', zipcode='85711'):
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.job = job
        self.zipcode = zipcode
        self.ratings = {}
        #self.movies = []

    @classmethod
    def load_users(cls, filename):
        fieldnames = ['user_id','age','gender','job', 'zipcode']
        users = {}
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter='|', fieldnames=fieldnames)
            for row in reader:
                user_id = row.pop('user_id')
                users[user_id] = User(**row)
        return users

    @classmethod
    def load_ratings(cls, filename, users):
        fieldnames = ['user_id','item_id','rating','timestamp']
        #ratings = {}
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter='\t', fieldnames=fieldnames)
            for row in reader:
                user_id = row['user_id']
                item_id = row['item_id']
                rating = row['rating']
                try:
                    users[user_id].ratings[item_id] = rating
                except KeyError:
                    assert KeyError("That user_id does not exist")
        return users
    @property
    def movies(self):
        try:
            return [item_id for item_id in self.ratings]
        except:
            assert KeyError("No movies found for this user")
