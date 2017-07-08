import csv
import numpy as np

def get_data(filename):
    result = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            result.append(row)
            #print(', '.join(row))

    return result


def append_row(filename, row):
    with open(filename, "a", newline="\n") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row)


def clear_data(filename):
    f = open(filename, "w+")
    f.close()


def save_data(filename, ndarray):
    with open(filename, "w", newline="\n") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for row in ndarray:
            writer.writerow(row)