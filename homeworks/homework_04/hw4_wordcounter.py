#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Process, Manager
from os import listdir
from collections import deque


def _count(path_to_dir, filename, result_dict):
    with open(path_to_dir + '/' + filename, 'r', encoding='utf8') as f:
        result_dict.update([(filename, len(f.read().split()))])


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    tasks_list = deque()
    result_dict = Manager().dict()
    try:
        for i in listdir(path_to_dir):
            task = Process(target=_count, args=(path_to_dir, i, result_dict))
            tasks_list.append(task)
            task.start()
    except FileNotFoundError:
        return
    for i in tasks_list:
        if i.is_alive():
            i.join()
    result_dict.update({"total": sum(result_dict.values())})
    return result_dict
