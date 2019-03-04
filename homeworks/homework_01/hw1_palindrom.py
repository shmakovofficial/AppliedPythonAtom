#!/usr/bin/env python
# coding: utf-8


def check_palindrom(input_string):
    length = len(input_string)
    for i in range(length // 2):
        if input_string[i] != input_string[length - i - 1]:
            return False
    return True
    '''
    Метод проверяющий строку на то, является ли
    она палиндромом.
    :param input_string: строка
    :return: True, если строка являестя палиндромом
    False иначе
    '''
