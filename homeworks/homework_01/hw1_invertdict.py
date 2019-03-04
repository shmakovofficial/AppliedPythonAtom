#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    result = {}
    def pushValue(key, value):
        if result.get(key) == None:
            result[key] = value
        elif isinstance(result[key], list):
            result[key].append(value)
        else:
            result[key] = [result[key], value]
    for key, value in source_dict:
        if isinstance(value, list) or isinstance(value, set) or isinstance(value, tuple):
            for i in value:
                pushValue(i, key)
        else:
            pushValue(value, key)
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
import pickle
with open("../../tests/tests_data/test_hw_01_invertdict.ini.pkl", "rb") as f:
    data = pickle.load(f)
print(data)
exit()

