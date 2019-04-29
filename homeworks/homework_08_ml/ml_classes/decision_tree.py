#!/usr/bin/env python
# coding: utf-8

import numpy as np


class DecisionTreeClassifier:
    '''
    Пишем свой велосипед - дерево для классификации
    '''

    def __init__(self, max_depth=None, min_leaf_size=None,
                 max_leaf_number=None, min_inform_criteria=None):
        '''
        Инициализируем наше дерево
        :param max_depth: один из возможных критерием останова - максимальная глубина дерева
        :param min_leaf_size: один из возможных критериев останова - число элементов в листе
        :param max_leaf_number: один из возможных критериев останова - число листов в дереве
        :param min_inform_criteria: один из критериев останова - процент прироста информации
        '''
        self.head = self.TreeNode(0)
        self.max_depth = max_depth
        self.min_leaf_size = min_leaf_size
        self.max_leaf_number = max_leaf_number
        self.min_inform_criteria = min_inform_criteria
        self.leaves = 0
        self.feature_list = None
        self.fitted = False
        self.classes = None

    def criteria(self, X, y, threshold, depth):
        if self._mic(X, y, threshold):
            print("Reached minimum information gain")
            return True
        if self._mln():
            print("Reached maximum leaf number")
            return True
        if self._mls(X.T, threshold):
            print("Reached minimum leaf size")
            return True
        if self._md(depth):
            print("Reached maximum depth")
            return True
        return False

    def _mic(self, X, y, threshold):
        if self.min_inform_criteria:
            return self.compute_split_information(X, y, threshold) < \
                   self.min_inform_criteria
        else:
            return False

    def _mln(self):
        if self.max_leaf_number:
            return self.leaves + 1 > self.max_leaf_number
        else:
            return False

    def _mls(self, X, threshold):
        if self.min_leaf_size:
            return (X[X <= threshold].shape[0] <= self.min_leaf_size or
                    X[X > threshold].shape[0] <= self.min_leaf_size)
        else:
            return False

    def _md(self, depth):
        if self.max_depth:
            return depth + 1 > self.max_depth
        else:
            return False

    def compute_split_information(self, X, y, th):
        '''
        Вспомогательный метод, позволяющий посчитать джини/энтропию для заданного разбиения
        :param X: Матрица (num_objects, 1) - срез по какой-то 1 фиче, по которой считаем разбиение
        :param y: Матрица (num_object, 1) - целевые переменные
        :param th: Порог, который проверяется
        :return: прирост информации
        '''
        count = len(X)
        count_left = len(X[X < th])
        count_right = count - count_left
        return (self.gini_impurity(y.T[0]) -
                (count_left / count * self.gini_impurity(y.T[0][:count_left]) +
                 count_right / count * self.gini_impurity(y.T[0][count_left:])))

    def create_feature_list(self, X):
        gini = np.zeros(X.shape[1])
        for i in range(X.shape[1]):
            values, counts = np.unique(X[:, i], return_counts=True)
            counts = counts / counts.sum()
            for j in counts:
                gini[i] -= j * np.log2(j)
        self.feature_list = np.argsort(gini)

    def gini_impurity(self, y):
        bins = np.bincount(y)
        return 1 - ((bins / bins.sum()) ** 2).sum()

    def fit(self, X, y):
        '''
        Стендартный метод обучения
        :param X: матрица объекто-признаков (num_objects, num_features)
        :param y: матрица целевой переменной (num_objects, 1)
        :return: None
        '''
        self.create_feature_list(X)
        self.classes = np.unique(y.T)
        self.head.X = X
        self.head.y = y
        self._fit_node(self.head)
        self.fitted = True

    def _fit_node(self, node):
        feature = self.feature_list[node.depth]
        indices = np.argsort(node.X[:, feature], axis=0)
        node.X = node.X[indices]
        node.y = node.y[indices]
        entropy = np.empty(node.X.shape[0])
        for i in range(entropy.shape[0]):
            entropy[i] = self.compute_split_information(node.X[:, feature],
                                                        node.y,
                                                        node.X[i, feature])
        threshold = node.X[np.argmax(entropy), feature]
        if not self.criteria(node.X[:, feature], node.y,
                             threshold, node.depth):
            print("Deepness is {}, leaves {}".format(node.depth, node.X.shape[0]))
            node.split(threshold, feature)
            print("Leaves left {}, right {}".format(node.left.X.shape[0], node.right.X.shape[0]))
            self.leaves += 1
            print("Going left from {}".format(feature))
            self._fit_node(node.left)
            print("Going right from {}".format(feature))
            self._fit_node(node.right)
            print("Going up from {}".format(feature))

    def predict(self, X):
        '''
        Метод для предсказания меток на объектах X
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказаний (num_objects, 1)
        '''
        probs = self.predict_proba(X)
        y = np.zeros(probs.shape[0], dtype=int)
        for i, j in enumerate(probs):
            y[i] = self.classes[np.argmax(j)]
        return y

    def predict_proba(self, X):
        '''
        метод, возвращающий предсказания принадлежности к классу
        :param X: матрица объектов-признаков (num_objects, num_features)
        :return: вектор предсказанных вероятностей (num_objects, 1)
        '''
        if not self.fitted:
            raise ValueError("Model is not fitted")
        y = np.empty((X.shape[0], self.classes.shape[0]))
        for i, j in enumerate(X):
            node = self.head.get_node(j)
            print(node.feature, node.threshold)
            classes = np.zeros(self.classes.shape)
            for k, l in enumerate(np.bincount(node.y.T[0])):
                classes[k] += l
            y[i] = classes / classes.sum()
        return y

    class TreeNode:
        def __init__(self, depth, threshold=None,
                     X=None, y=None, left=None, right=None):
            self.depth = depth
            self.left = left
            self.right = right
            self.threshold = threshold
            self.X = X
            self.y = y
            self.feature = None

        def split(self, threshold, feature):
            self.threshold = threshold
            self.feature = feature
            self.set_left(threshold, feature)
            self.set_right(threshold, feature)
            self.X = None
            self.y = None

        def set_left(self, threshold, feature):
            self.left = DecisionTreeClassifier.TreeNode(
                depth=self.depth + 1,
                X=self.X[self.X[:, feature] <= threshold],
                y=self.y[self.X[:, feature] <= threshold])

        def set_right(self, threshold, feature):
            self.right = DecisionTreeClassifier.TreeNode(
                depth=self.depth + 1,
                X=self.X[self.X[:, feature] > threshold],
                y=self.y[self.X[:, feature] > threshold])

        def get_node(self, x):
            print("On the node with deepness {}, feature {}, threshold {}".format(
                self.depth, self.feature, self.threshold))
            if self.feature is not None:
                if x[self.feature] <= self.threshold:
                    print("Going to the left")
                    return self.left.get_node(x)
                else:
                    print("Going to the right")
                    return self.right.get_node(x)
            else:
                print("Found!")
                return self
