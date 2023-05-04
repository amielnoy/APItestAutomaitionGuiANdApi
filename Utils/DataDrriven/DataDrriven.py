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
    test_data = {}
    try:
        with open(file_full_path, newline="") as csvfile:
            data = csv.reader(csvfile, delimiter=",")
            next(data)  # skip header row
            for row in data:
                test_data[row.split(',')[0]] = row
        return test_data

    except FileNotFoundError:
        print('File not found', file_full_path)

    except Exception as e:
        print(e)
