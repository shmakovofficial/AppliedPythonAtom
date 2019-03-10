import json
import csv


def _is_json(filename, charset):
    try:
        with open(filename, encoding=charset) as f:
            json.load(f)
    except json.JSONDecodeError:
        return False
    return True


def _is_tsv(filename, charset):
    with open(filename, encoding=charset) as f:
        s = csv.reader(f, delimiter="\t")
        length = 0
        for i in s:
            if length != 0 and length != len(i):
                return False
            length = len(i)
    return True


def formation(filename, charset):
    if _is_json(filename, charset):
        return 'json'
    elif _is_tsv(filename, charset):
        return 'tsv'
    else:
        raise SystemExit("Формат не валиден")
