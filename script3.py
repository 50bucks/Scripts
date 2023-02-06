import csv

def read_data_from_csv(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def print_data(data):
    for row in data:
        print(f"ID: {row[0]}, String: {row[1]}")

def calculate_average_string_length(data):
    total_length = 0
    for row in data:
        total_length += len(row[1])
    average_length = total_length / len(data)
    return average_length

file_name = "strings.csv"
data = read_data_from_csv(file_name)
print("Data from file:")
print_data(data)
average_length = calculate_average_string_length(data)
print(f"Average string length: {average_length}")
