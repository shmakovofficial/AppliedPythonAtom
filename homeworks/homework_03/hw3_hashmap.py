#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    LOAD_FACTOR = 2 / 3
    RESIZE_FACTOR = 2
    count = 0

    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self.key = key
            self.value = value

        def get_key(self):
            # TODO возвращаем ключ
            return self.key

        def get_value(self):
            # TODO возвращаем значение
            return self.value

        def __eq__(self, other):
            # TODO реализовать функцию сравнения
            return self.key == other.key

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.bucket_count = bucket_num
        self.bucket_list = [[]] * self.bucket_count

    def get(self, key, default_value=None):
        # TODO метод get, возвращающий значение,
        #  если оно присутствует, иначе default_value
        other = self.Entry(key, key)
        for i in self.bucket_list[self._get_index(self._get_hash(key))]:
            if i == other:
                return i.get_value()
        return default_value

    def put(self, key, value):
        # TODO метод put, кладет значение по ключу,
        #  в случае, если ключ уже присутствует он его заменяет
        other = self.Entry(key, value)
        index = self._get_index(self._get_hash(key))
        for i, j in enumerate(self.bucket_list[index]):
            if j == other:
                self.bucket_list[index].pop(i)
                self.bucket_list[index].insert(i, other)
                return
        self.bucket_list[index].append(other)
        self.count += 1

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.count

    def _get_hash(self, key):
        # TODO Вернуть хеш от ключа,
        #  по которому он кладется в бакет
        return hash(key)

    def _get_index(self, hash_value):
        # TODO По значению хеша вернуть индекс элемента в массиве
        return hash_value % self.bucket_count

    def values(self):
        # TODO Должен возвращать итератор значений
        return self._ValuesIterator(self.bucket_list, self.bucket_count)

    def keys(self):
        # TODO Должен возвращать итератор ключей
        return self._KeysIterator(self.bucket_list, self.bucket_count)

    def items(self):
        # TODO Должен возвращать итератор пар ключ и значение (tuples)
        return self._Iterator(self.bucket_list, self.bucket_count)

    def _filled_buckets(self):
        return sum([1 for i in self.bucket_list if len(i) > 0])

    def _resize(self):
        # TODO Время от времени нужно ресайзить нашу хешмапу
        if self._filled_buckets() > self.bucket_count * self.LOAD_FACTOR:
            new_map = HashMap(self.bucket_count * self.RESIZE_FACTOR)
            for i in self.items():
                new_map.put(*i)
            del self.bucket_list
            self.bucket_list = new_map.bucket_list
            self.bucket_count *= 2

    def __str__(self):
        # TODO Метод выводит "buckets: {}, items: {}"
        output = ""
        output += "buckets:{"
        for i, j in enumerate(self.bucket_list):
            if len(j) > 0:
                output += " {},".format(i)
        output += "}, items: {"
        for i in self.items():
            output += " {},".format(i)
        output += "}"
        return output.replace(",}", "}")

    def __contains__(self, item):
        return item in self.keys()

    class _Iterator:
        def __init__(self, iterable, limit):
            self.bucket_list = iterable
            self.bucket_index = 0
            self.list_index = 0
            self.map_capacity = limit

        def __iter__(self):
            return self

        def _position(self):
            while self.bucket_index < self.map_capacity:
                if self.list_index < \
                        len(self.bucket_list[self.bucket_index]):
                    return
                else:
                    self.list_index = 0
                    self.bucket_index += 1

        def __next__(self):
            try:
                item = \
                    self.bucket_list[self.bucket_index][self.list_index]
            except IndexError:
                raise StopIteration
            self.list_index += 1
            self._position()
            return item.get_key(), item.get_value()

    class _KeysIterator(_Iterator):

        def __next__(self):
            return super().__next__()[0]

    class _ValuesIterator(_Iterator):

        def __next__(self):
            return super().__next__()[1]
