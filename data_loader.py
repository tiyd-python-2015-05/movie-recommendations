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
        headers = next(reader)
        print(headers)
        print("---")
        for row in reader:
            print(row)

if __name__ == '__main__':
    load_data()
