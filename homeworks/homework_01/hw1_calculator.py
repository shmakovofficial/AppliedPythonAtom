#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if operator == "plus":
        if x.isdigit() and y.isdigit():
            return x + y
        else:
            return None
    elif operator == "minus":
        if x.isdigit() and y.isdigit():
            return x - y
        else:
            return None
    elif operator == "mult":
        if x.isdigit() and y.isdigit():
            return x * y
        else:
            return None
    elif operator == "divide":
        if x.isdigit() and y.isdigit():
            return x / y if y != 0 else None
        else:
            return None
    else:
        return None
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''
