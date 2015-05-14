import csv

def file_open_read_data_list(data_file):
    with open(data_file, encoding='windows-1252') as file:
        reader = csv.reader(file, delimiter='\t')
        data_list = [i for i in reader]
    return data_list

def file_open_read_item_list(item_file):
    with open(item_file, encoding='windows-1252') as file:
        reader = csv.reader(file, delimiter="|")
        data_list = [i for i in reader]
    return data_list

def csv_data_into_user_dictionary():
    pass

#    for row in reader:
#        print row
if __name__ == "__main__":
    data_file = "u.sampledata"
    item_file = "u.sampleitem"
    print(file_open_read_data_dict(data_file))
    print(file_open_read_item_dict(item_file))
