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
        merged_list = list()
        for i in list_of_lists:
            merged_list += i
        merged_list = list(map(lambda x: (x, x), merged_list))
        h = MaxHeap(merged_list)
        result = list()
        for i in range(k):
            result.append(h.extract_maximum()[0])
        return result
