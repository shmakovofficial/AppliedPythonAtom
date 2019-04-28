#!/usr/bin/env python
# coding: utf-8

import numpy as np


class KNNRegressor:
    """
    Построим регрессию с помощью KNN. Классификацию писали на паре
    """

    def __init__(self, n):
        '''
        Конструктор
        :param n: число ближайших соседей, которые используются
        '''
        self.n = n
        self.x = None
        self.y = None
        self.fitted = False

    def fit(self, x, y):
        '''
        :param x: обучающая выборка, матрица размерности (num_obj, num_features)
        :param y: целевая переменная, матрица размерности (num_obj, 1)
        :return: None
        '''
        self.x = x
        self.y = y
        self.fitted = True

    def predict(self, X):
        '''
        :param X: выборка, на которой хотим строить предсказания (num_test_obj, num_features)
        :return: вектор предсказаний, матрица размерности (num_test_obj, 1)
        '''
        y = []
        assert len(X.shape) == 2
        for t in X:
            # Посчитаем расстояние от всех элементов в тренировочной выборке
            # до текущего примера -> результат - вектор размерности трейна
            d = np.linalg.norm(self.x - t, ord=2, axis=1)
            # Возьмем индексы n элементов, расстояние до которых минимально
            # результат -> вектор из n элементов
            idx = np.argsort(d)[:self.n]
            if np.isclose(d[idx[0]], 0):
                y.append(self.y[idx[0]][0])
            else:
                prediction = 0
                inverted_distance = (1 / d[idx]).sum()
                for i in idx:
                    prediction += self.y[i][0] / d[i]
                y.append(prediction / inverted_distance)
        return y


if __name__ == "__main__":
    # y = x * 5
    # для четного числа соседей mse будет почти нулевой
    # ввиду симметричности выборок
    for number in range(1, 10):
        a = np.empty((50, 1))
        b = np.empty((50, 1))
        c = np.empty((50 - number * 2, 1))
        for i in range(0, 50):
            a[i][0] = i * 2
            b[i][0] = (i * 2) * 5
        knn = KNNRegressor(number)
        knn.fit(a, b)
        test = np.empty((50, 1))
        for i in range(0, 50 - number * 2):
            c[i][0] = (i + number) * 2 + 1
        print("For {} neighbors MSE is {}".format(
            number, ((np.array(knn.predict(c)) - c.T[0] * 5) ** 2).mean()))
