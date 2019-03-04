#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    if number < 0:
        return -1 * int(str(number)[:0:-1])
    else:
        return int(str(number)[::-1])
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
