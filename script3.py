import csv
import argparse
import os
import re

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

def normalize_csv(input_file, delimiter='|', quotechar='"'):
    output_file = input_file.replace('.csv', '_normalized.csv')
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        reader = csv.reader(in_file, delimiter=delimiter)
        writer = csv.writer(out_file, delimiter=',', quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)

        for row in reader:
            new_row = [quotechar + item.replace(quotechar, quotechar * 2) + quotechar if ',' in item else item for item in row]
            writer.writerow(new_row)

    return output_file

def detect_delimiter_and_quotechar(input_file):
    with open(input_file, 'r') as f:
        first_line = f.readline()
        delimiters = [',', '|', '\t']
        quotechars = ['"', "'"]

        for delimiter in delimiters:
            if delimiter in first_line:
                break
        else:
            delimiter = None

        for quotechar in quotechars:
            pattern = re.compile(f'{quotechar}[^{quotechar}]*{quotechar}')
            if pattern.search(first_line):
                break
        else:
            quotechar = None

    return delimiter, quotechar

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Normalize a CSV file')
    parser.add_argument('input_file', help='The input CSV file')
    parser.add_argument("-d", "--delimiter", help="The input delimiter", default="|")
    parser.add_argument("-q", "--quotechar", help="The quote character", default='"')
    parser.add_argument("-o", "--output_file", help="The path to the output CSV file")
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: The file {args.input_file} does not exist')
        exit(1)

    delimiter = args.delimiter if args.delimiter != "detect" else detect_delimiter_and_quotechar(args.input_file)[0]
    quotechar = args.quotechar if args.quotechar != "detect" else detect_delimiter_and_quotechar(args.input_file)[1]
    
    data = read_data_from_csv(args.input_file)
    print_data(data)
    average_length = calculate_average_string_length(data)
    print(f"Average string length: {average_length:.2f}")

    if args.output_file:
        output_file = normalize_csv(args.input_file, delimiter, quotechar, args.output_file)
        print(f'Normalized data written to {output_file}')
    else:
        normalize_csv(args.input_file, delimiter, quotechar)
