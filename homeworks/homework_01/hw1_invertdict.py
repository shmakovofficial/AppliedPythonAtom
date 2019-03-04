#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    new_dict = {}
    if not isinstance(source_dict, dict):
        return dict()

    def pushValue(key, value):
        if new_dict.get(key) is None:
            new_dict[key] = value
        elif isinstance(new_dict[key], list):
            new_dict[key].append(value)
        else:
            new_dict[key] = [new_dict[key], value]
    for key, value in source_dict.items():
        if (isinstance(value, list) or isinstance(value, set) or
                isinstance(value, tuple)):
            for i in value:
                pushValue(i, key)
        else:
            pushValue(value, key)
    return new_dict
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
