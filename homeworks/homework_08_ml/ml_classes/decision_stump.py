#!/usr/bin/env python
# coding: utf-8

import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self.le_y = None
        self.gt_y = None
        self.threshold = None
        self.length = None
        self.fitted = False
        self.predict_vector = np.vectorize(self.decide)

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        # сортируем значения
        self.length = X.shape[0]
        values_id = np.argsort(X)
        sorted_values = np.vstack((X[values_id], y[values_id]))
        # три массива для хранения средних значений и ошибок
        le_means = np.empty(self.length)
        le_means2 = np.empty(self.length)
        gt_means = np.empty(self.length)
        gt_means2 = np.empty(self.length)
        mse = np.empty(self.length)
        mse2 = np.empty(self.length)
        # заполнение начальными значениями
        le_means[0] = np.nan
        le_means2[0] = le_means[0]
        gt_means[0] = y.mean()
        gt_means2[0] = gt_means[0]
        mse[0] = ((y - gt_means[0]) ** 2).mean()
        mse2[0] = mse[0]
        # заполнение массивов в цикле с пересчетом за константное время
        for i in range(1, self.length):
            le_means[i] = self.le_mean_new(
                le_means[i - 1],
                i,
                sorted_values[1][i - 1]
            )
            if i == 1:
                le_means2[1] = sorted_values[1][0]
            else:
                le_means2[i] = sorted_values[1][:i].mean()
            gt_means[i] = self.gt_mean_new(
                gt_means[i - 1],
                self.length,
                i,
                sorted_values[1][i - 1]
            )
            gt_means2[i] = sorted_values[1][i:].mean()
            mse2[i] = (((sorted_values[1][:i] - le_means[i]) ** 2).sum() +
                       ((sorted_values[1][i:] - gt_means[i]) ** 2).sum() /
                       self.length)
            mse[i] = self.mse_new(
                mse[i - 1],
                i,
                le_means[i - 1],
                le_means[i],
                gt_means[i - 1],
                gt_means[i],
                self.length
            )

        # выбор параметров с наименьшей ошибкой
        min_index = np.argmin(mse)
        if min_index == 0:
            self.le_y = le_means[0]
            self.threshold = sorted_values[0][self.length - 1]
            self.gt_y = np.nan
        else:
            self.le_y = le_means[min_index]
            self.threshold = (sorted_values[0][min_index - 1] +
                              sorted_values[0][min_index]) / 2
            self.gt_y = gt_means[min_index]
        self.fitted = True

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        if not self.fitted:
            raise ValueError("Model is not fitted")
        return self.predict_vector(X)

    def decide(self, x):
        if x <= self.threshold:
            return self.le_y
        else:
            return self.gt_y

    def le_mean_new(self, le_mean_old, index, value):
        if np.isnan(le_mean_old):
            return value
        else:
            return (le_mean_old * (index - 1) + value) / index

    def gt_mean_new(self, gt_mean_old, length, index, value):
        return (gt_mean_old * (length - index + 1) - value) / (length - index)

    def mse_new(self, mse_old, index, le_mean_old, le_mean_new,
                gt_mean_old, gt_mean_new, length):
        if index == 1:
            return (mse_old +
                    (length * (gt_mean_old ** 2) -
                     le_mean_new ** 2 -
                     (length - 1) * (gt_mean_new ** 2)) / length)
        else:
            return (mse_old +
                    ((index - 1) * (le_mean_old ** 2) +
                     (length - index + 1) * (gt_mean_old ** 2) -
                     index * (le_mean_new ** 2) -
                     (length - index) * (gt_mean_new ** 2)) / length)


if __name__ == "__main__":
    a = np.array([0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0])
    b = np.array([i for i in range(16)])
    np.random.shuffle(b)
    a = a[b]
    c = np.array([i for i in range(0, 12, 3)])
    dst = DecisionStumpRegressor()
    dst.fit(b, a)
    print(c)
    print(dst.predict(c))
