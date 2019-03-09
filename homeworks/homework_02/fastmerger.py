#!/usr/bin/env python
# coding: utf-8

from .heap import MaxHeap


class FastSortedListMerger:

    @staticmethod
    def merge_first_k(list_of_lists, k):
        '''
        принимает на вход список отсортированных непоубыванию списков и число
        на выходе выдает один список длинной k, отсортированных по убыванию
        '''
        local_list = [i[:] for i in list_of_lists]
        h = MaxHeap([(j.pop(), i) for i, j in enumerate(local_list)
                     if len(j) > 0])
        result = list()
        for i in range(k):
            try:
                item = h.extract_maximum()
            except IndexError:
                return result
            result.append(item[0])
            if len(local_list[item[1]]) > 0:
                h.add((local_list[item[1]].pop(), item[1]))
        return result
