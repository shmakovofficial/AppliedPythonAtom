#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    return -1 * int(str(number)[:0:-1]) if number<0 else int(str(number)[::-1])
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
