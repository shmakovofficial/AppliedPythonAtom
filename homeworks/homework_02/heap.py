#!/usr/bin/env python
# coding: utf-8


class Heap:

    def __init__(self, array):
        self.data = array[:]
        self.build_heap()

    def add(self, elem_with_priority):
        self.data.append(elem_with_priority)
        self.build_heap()

    def build_heap(self):
        if len(self.data):
            for i in reversed(range(len(self.data) // 2)):
                self._sift_down(i)

    def _sift_down(self, index: int):
        max_index = self._get_max_index(index, index * 2 + 1)
        max_index = self._get_max_index(max_index, index * 2 + 2)
        if max_index != index:
            self.data[index], self.data[max_index] = \
                self.data[max_index], self.data[index]
            self._sift_down(max_index)

    def _get_max_index(self, i: int, j: int):
        if i < len(self.data):
            if j < len(self.data):
                return i if comparator_d(self.data[i], self.data[j]) else j
            else:
                return i
        else:
            if j < len(self.data):
                return j
            else:
                return None


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def extract_maximum(self):
        max_element = self.data.pop(0)
        self.build_heap()
        return max_element


def comparator_d(x, y):
    if x[0] == y[0]:
        return x[1] >= y[1]
    elif x[0] > y[0]:
        return True
    else:
        return False
