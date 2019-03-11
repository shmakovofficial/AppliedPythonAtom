import csv
from file_tools import printing


def print_tsv(filename, charset):
    s = list()
    with open(filename, encoding=charset) as file:
        sr = csv.reader(file, delimiter="\t")
        for i in sr:
            if len(i) == 0:
                raise ValueError("Формат не валиден")
            s.append(i)
    printing(s)
