#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    for i in range(10):
        input_string = input_string.replace(str(i) + " ", str(i) + "|")
    while " " in input_string:
        input_string = input_string.replace(" ", "")
    while "\t" in input_string:
        input_string = input_string.replace("\t", "")
    while "--" in input_string:
        input_string = input_string.replace("--", "+")
    while "++" in input_string:
        input_string = input_string.replace("++", "+")
    while "+-" in input_string:
        input_string = input_string.replace("+-", "-")
    while "(-" in input_string:
        input_string = input_string.replace("(-", "(0-")
    while "/-" in input_string:
        input_string = input_string.replace("/-", "*(0-1)/")
    while "*-" in input_string:
        input_string = input_string.replace("*-", "*(0-1)*")
    if len(input_string) > 0 and (input_string[0] is
                                  "-" or input_string[0] is "+"):
        input_string = "0" + input_string
    item = ""
    output_list = []
    stak = []

    def is_foo(operator):
        return (operator is "+" or operator is "-" or
                operator is "/" or operator is "*")

    while len(input_string) > 0:
        if is_foo(input_string[0]):
            if len(item) > 0:
                try:
                    output_list.append(float(item))
                    item = ""
                except (TypeError, ValueError):
                    return None
            while len(stak) > 0 and stak[len(stak) - 1] is not "(":
                if (stak[len(stak) - 1] is "*" or input_string[0] is "+" or
                        stak[len(stak) - 1] is "/" or input_string[0] is "-"):
                    output_list.append(stak.pop())
                else:
                    break
            stak.append(input_string[0])
            input_string = input_string[1:]
        elif input_string[0] is "(":
            if len(item) > 0:
                return None
            stak.append("(")
            input_string = input_string[1:]
        elif input_string[0] is ")":
            if len(item) == 0:
                return None
            try:
                output_list.append(float(item))
                item = ""
            except (TypeError, ValueError):
                return None
            input_string = input_string[1:]
            try:
                item = stak.pop()
                while item is not "(":
                    output_list.append(item)
                    item = stak.pop()
                item = ""
            except IndexError:
                return None
        elif input_string[0].isdigit() or input_string[0] is ".":
            item += input_string[0]
            input_string = input_string[1:]
        elif input_string[0] is "|":
            output_list.append(float(item))
            item = ""
            input_string = input_string[1:]
        else:
            return None
    if len(item) > 0:
        try:
            output_list.append(float(item))
            item = ""
        except (ValueError, TypeError):
            return None
    while len(stak) > 0:
        output_list.append(stak.pop())
    try:
        while len(output_list) > 0:
            item = output_list.pop(0)
            if isinstance(item, float):
                stak.append(item)
            else:
                item2 = stak.pop()
                item1 = stak.pop()
                if item is "+":
                    stak.append(item1 + item2)
                elif item is "-":
                    stak.append(item1 - item2)
                elif item is "/":
                    try:
                        stak.append(item1 / item2)
                    except ZeroDivisionError:
                        return None
                elif item is "*":
                    stak.append(item1 * item2)
    except IndexError:
        return None
    if len(stak) != 1:
        return None
    return stak[0]
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''
