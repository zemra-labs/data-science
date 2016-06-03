import pandas

def add_full_name(path_to_csv, path_to_new_csv):


    baseball_data = pandas.read_csv(path_to_csv)

    baseball_data['nameFull'] = baseball_data['nameFirst'] + " " + baseball_data['nameLast']

    baseball_data.to_csv(path_to_new_csv)


if __name__ == "__main__":

    path_to_csv = ""
    path_to_new_csv = ""
    add_full_name(path_to_csv, path_to_new_csv)
