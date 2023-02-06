import csv
import random
import string
import argparse

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_csv(rows, filename, string_length):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'random_string'])
        for i in range(rows):
            random_string = generate_random_string(string_length)
            writer.writerow([i, random_string])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, required=True, help='Number of rows to generate')
    parser.add_argument('--filename', type=str, required=True, help='File name for the CSV')
    parser.add_argument('--string_length', type=int, default=10, help='Length of the random string to generate')
    args = parser.parse_args()

    generate_csv(args.rows, args.filename, args.string_length)
