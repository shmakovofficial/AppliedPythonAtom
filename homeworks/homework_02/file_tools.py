import json
import csv


def testing(filename):
    try:
        f = open(filename)
        f.close()
    except FileNotFoundError:
        raise SystemExit("File not found")


def _parse_to_list(filename, file_charset, file_format):
    with open(filename, encoding=file_charset) as f:
        s = list()
        if file_format == 'json':
            sr = json.load(f)
            s.append(list(sr[0].keys()))
            for i in sr:
                s.append(list(i.values()))
        else:
            sr = csv.reader(f, delimiter="\t")
            for i in sr:
                s.append(i)
    return s


def printing(filename, file_charset, file_format, headers=True):
    list_of_lists = _parse_to_list(filename, file_charset, file_format)
    if len(list_of_lists) < 1:
        print("Формат не валиден")
        return None
    for i in list_of_lists:
        if len(i) != len(list_of_lists[0]):
            print("Формат не валиден")
            return None
    lengths = list()
    for i in range(len(list_of_lists[0])):
        current_length = 0
        for j in list_of_lists:
            current_length = max(len(str(j[i])), current_length)
        lengths.append(current_length)
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))
    if headers:
        data_headers = list_of_lists.pop(0)
        for i, j in enumerate(data_headers):
            print("|  {:^{width}}  ".format(j, width=lengths[i]), end='')
        print("|")
    for i in list_of_lists:
        for j, k in enumerate(i):
            output = "|  {:" + (">" if j == len(i) - 1 else "<") + "{width}}  "
            print(output.format(k, width=lengths[j]), end='')
        print("|")
    print("-" * (sum(lengths) + 5 * len(lengths) + 1))