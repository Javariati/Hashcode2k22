import csv
import pandas as pd


def import_csv(filename, delimiter=' '):
    data = []

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        for row in csv_reader:
            data.append(row)

    return data


def import_csv2(filename):
    header = pd.read_csv(filename, header=None, nrows=1, sep=' ')

    df = pd.read_csv(filename, header=None, skiprows=1, nrows=header[0], sep='\n')
    df = df[0].str.split('\s\|\s', expand=True)