#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    if str(x).isdigit() and str(y).isdigit():
        x, y = float(x), float(y)
        if operator == "plus":
            return x + y
        elif operator == "minus":
            return x - y
        elif operator == "mult":
            return x * y
        elif operator == "divide":
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
