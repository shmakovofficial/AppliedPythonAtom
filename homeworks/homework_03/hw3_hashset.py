#!/usr/bin/env python
# coding: utf-8

from .hw3_hashmap import HashMap


class HashSet(HashMap):

    def __init__(self):
        # TODO Сделать правильно =)
        super().__init__()

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        other = self.Entry(key, key)
        for i in self.bucket_list[self._get_index(self._get_hash(key))]:
            if i == other:
                return True
        return False

    def put(self, key, value=None):
        # TODO метод put, нужно переопределить данный метод
        super().put(key, None)

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return super().__len__()

    def values(self):
        # TODO возвращать итератор значений
        return super().keys()

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        new_set = HashSet()
        for i in super().keys():
            if i in another_hashset:
                new_set.put(i)
        return new_set
