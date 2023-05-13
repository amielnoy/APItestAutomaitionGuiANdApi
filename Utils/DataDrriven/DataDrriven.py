import csv

def read_test_data_from_csv_to_list(file_full_path):
    test_data = []
    try:
        with open(file_full_path, newline="") as csvfile:
            data = csv.reader(csvfile, delimiter=",")
            next(data)  # skip header row
            for row in data:
                test_data.append(row)
        return test_data

    except FileNotFoundError:
        print('File not found', file_full_path)

    except Exception as e:
        print(e)


def read_test_data_from_csv_to_dictionary(file_full_path):
    dict_array = []
    try:
        with open(file_full_path, 'r') as data:
            for line in csv.DictReader(data):
                dict_array.append(line)

        return dict_array

    except FileNotFoundError:
        print('File not found', file_full_path)

    except Exception as e:
        print(e)


def read_data_from_csv(file_full_path):
    try:
        with open(file_full_path, newline='') as csvfile:
            data = csv.DictReader(csvfile)
            return [row for row in data]

    except FileNotFoundError:
        print('File not found', file_full_path)

    except Exception as e:
        print(e)
