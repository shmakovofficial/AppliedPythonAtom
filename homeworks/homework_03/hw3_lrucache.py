#!/usr/bin/env python
# coding: utf-8
import time


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        # TODO инициализация декоратора
        #  https://www.geeksforgeeks.org/class-as-decorator-in-python/
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = list()
        self.length = 0
        self.func = 2

    def __call__(self, function):
        # TODO вызов функции
        self.function = function

        def _strip_cache():
            if self.maxsize > 0:
                while self.length > self.maxsize:
                    self.cache.pop()
                    self.length -= 1

        def _cached_index(arg):
            for i, j in enumerate(self.cache):
                if j['item'] == arg:
                    return i

        def _dec(item):
            index = _cached_index(item)
            if index is not None:
                temp = self.cache.pop(index)
                if self.ttl and \
                        temp['time'] < int(time.time() * 1000.0) - self.ttl:
                    temp = {
                        'item': item,
                        'result': self.function(item),
                        'time': int(time.time() * 1000.0)
                    }
            else:
                temp = {
                    'item': item,
                    'result': self.function(item),
                    'time': int(time.time() * 1000.0)
                }
                self.length += 1
            self.cache.insert(0, temp)
            _strip_cache()
            return temp['result']

        return _dec
