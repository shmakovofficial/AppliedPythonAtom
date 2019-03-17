#!/usr/bin/env python
# coding: utf-8


def groupping_anagramms(words):
    """
    Функция, которая группирует анаграммы.
    Возвращаем массив, где элементом является массив с анаграмами.
    Пример:  '''Аз есмь строка живу я мерой остр
                За семь морей ростка я вижу рост
                Я в мире сирота
                Я в Риме Ариост'''.split()
                ->
                [
                 ['Аз'], ['есмь', 'семь'],
                 ['строка', 'ростка'], ['живу', 'вижу'],
                 ['я', 'я'], ['мерой', 'морей'],
                 ['остр)'], ['За'], ['рост'], ['Я', 'Я'],
                 ['в', 'в'], ['мире'], ['сирота'],
                 ['Риме'], ['Ариост']
                ]
    :param words: list of words (words in str format)
    :return: list of lists of words
    """

    # TODO: реализовать функцию
    result = []
    for i, j in enumerate(words):
        if j is None:
            result.append(None)
            continue
        result.append([j])
        for m in range(i + 1, len(words)):
            if words[m] is not None and \
                    ''.join(sorted(j.lower())) == \
                    ''.join(sorted(words[m].lower())):
                result[i].append(words[m])
                words[m] = None
    return [i for i in result if i is not None]
