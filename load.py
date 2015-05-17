import csv


def loader():

    movie_dict = {}
    ratings = {}

    with open('/Users/briandeshazer/Desktop/ml-100k/u.item',\
     endcoding='windows-1252') as file:
     movies = csv.reader(file, delimiter='|')

     for item in movies:
         movie_dict[int(item[0])] = item[1]

    with open('/Users/briandeshazer/Desktop/ml-100k/u.data',\
    endcoding='windows-1252') as file:
    data = csv.reader(file, delimiter='\t')

    for item in data:
        item = list(map(int,item))
        ratings[(item[0], item[1])] = item[2]

    return movie_dict, ratings
