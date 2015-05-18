import csv



def read_u_item_dict(data_file):
    with open(data_file, encoding='windows-1252') as csvfile:
        fieldnames = ['movie id', 'movie title', 'release date', 'movie release date'
                    , 'video release date', 'IMDB URL', 'unknown', 'action', 'adventure', 'Animation',
                        'childrens', 'comedy', 'crime', 'documentary', 'drama', 'fantasy', 'film-noir'
                        , 'horror', 'musical', 'mystery', 'romance', 'sci-fy', 'thriller',
                        'war', 'western']
        reader = csv.DictReader(csvfile, delimiter = '|', fieldnames = fieldnames)
        item_dict = [row for row in reader]
        return item_list

def read_u_data_dict(item_file):
    with open(item_file, encoding='windows-1252') as csvfile:
        fieldnames = ['user id','item id', 'rating', 'timestamp']
        reader =  csv.DictReader(csvfile, delimiter = '\t', fieldnames = fieldnames)
        data_dict = [row for row in reader]
        return data_list

def read_u_item_list(item_file):
    with open(item_file, encoding='windows-1252') as csvfile:
        reader = csv.reader(csvfile, delimiter = '|')
        item_list = [row for row in reader]
        return item_list

def read_u_data_list(data_file):
    with open(data_file, encoding='windows-1252') as csvfile:
        reader = csv.reader(csvfile, delimiter = '\t')
        data_list = [row for row in reader]
        return data_list

        #proof that itemID = movieID
        # user_id = [item[1] for item in data_list]
        # sorted_user_id = sorted(user_id)
        # print(sorted_user_id)

def find_average_rating_of_movie_by_ID(rating_dict):
    average_dict = rating_dict.copy()
    for key, value in average_dict.items():
        if len(value) >= 5:
            average_value = sum(value) / len(value)
            average_dict[key] = average_value
        else:
            continue
    return average_dict



def find_ratings_by_ID(data_list):
    ratings = [[list[1],list[2]] for list in data_list]
    rating_dict = {}
    for ID, rating in ratings:
        rating_dict.setdefault(ID, []).append(int(rating))
    return rating_dict

def find_movie_name_by_ID(item_list):
    movie_name = {list[0]:list[1] for list in item_list}
    return movie_name


def find_all_ratings_of_user(data_list):
    info = [[list[0],{list[1]:list[2]}] for list in data_list]
    user_dict = {}
    for User, movie_ID in info:
        user_dict.setdefault(User, []).append(movie_ID)
    return user_dict




if __name__=='__main__':
    item_file = 'u.item'
    data_file = 'u.data'
    item_list = read_u_item_list(item_file)
    data_list = read_u_data_list(data_file)
    rating_dict = find_ratings_by_ID(data_list)
    print(find_average_rating_of_movie_by_ID(rating_dict))
    print(find_all_ratings_of_user(data_list))
