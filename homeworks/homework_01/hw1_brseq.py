#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    lookup = []
    for i in input_string:
        if i == "[" or i == "{" or i == "(":
            lookup.append(i)
        elif i == "]":
            if lookup.pop() != "[":
                return False
        elif i == "}":
            if lookup.pop() != "{":
                return False
        elif i == ")":
            if lookup.pop() != "(":
                return False
        else:
            return False
    return True
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''
