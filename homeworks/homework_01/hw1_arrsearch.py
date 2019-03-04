#!/usr/bin/env python
# coding: utf-8


def find_indices(input_list, n):
    lookup = {}
    count = 0
    for i in input_list:
        if (n - i) in lookup.keys():
            return count, lookup[n - i]
        else:
            lookup[i] = count
        count += 1
    return None
    '''
    Метод возвращает индексы двух различных
    элементов listа, таких, что сумма этих элементов равна
    n. В случае, если таких элементов в массиве нет,
    то возвращается None
    Ограничение по времени O(n)
    :param input_list: список произвольной длины целых чисел
    :param n: целевая сумма
    :return: tuple из двух индексов или None
    '''
