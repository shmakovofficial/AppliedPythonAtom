#!/usr/bin/env python
# coding: utf-8

import numpy as np
from metrics import mse


class LinearRegression:
    def __init__(self, lambda_coefficient=0.1, regularization=None,
                 alpha=0.1, n_iter=1000, delta=0.1):
        """
        :param lambda_coefficient: constant for gradient descent step
        :param regularization: regularization type ("L1" or "L2") or None
        :param alpha: regularization coefficient
        """
        self.lambda_coefficient = lambda_coefficient
        self.fitted = False
        self.weights = None
        self.n_iter = n_iter
        self.delta = delta
        self.alpha = alpha
        self.regularization = regularization

    def _loss(self, x, y):
        if self.regularization == "L1":
            return (mse(y, x @ self.weights) +
                    self.alpha * np.linalg.norm(self.weights[1:].T, ord=1))
        elif self.regularization == "L2":
            return (mse(y, x @ self.weights) +
                    self.alpha * np.linalg.norm(self.weights[1:].T))
        else:
            return mse(y, x @ self.weights)

    def _mse_grad(self, x, y):
        return (2 / y.shape[0] *
                ((x @ self.weights - y).T @ x).reshape((-1, 1)))

    def _loss_grad(self, x, y):
        if self.regularization == "L1":
            return (self._mse_grad(x, y) +
                    self.alpha * np.sign(self.weights[1:])).reshape((-1, 1))
        elif self.regularization == "L2":
            return (self._mse_grad(x, y) +
                    2 * self.alpha * self.weights[1:]).reshape((-1, 1))
        else:
            return self._mse_grad(x, y)

    def fit(self, x_train, y_train):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x = np.hstack((np.ones((x_train.shape[0], 1)), x_train))
        self.weights = np.ones((x.shape[1], 1))
        count = 0
        while count < self.n_iter:
            self.weights -= (self.lambda_coefficient *
                             self._loss_grad(x, y_train))
            if self._loss(x, y_train) < self.delta:
                break
            count += 1
        self.fitted = True

    def predict(self, x_test):
        """
        Predict using model.
        :param x_test: test data for predict in
        :return: y_test: predicted values
        """
        if not self.fitted:
            raise Exception("Model is not fitted")
        else:
            if x_test.shape[1] != self.weights.shape[0] - 1:
                raise ValueError
            else:
                return (np.hstack((np.ones((x_test.shape[0], 1)), x_test)) @
                        self.weights)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if not self.fitted:
            raise Exception("Model is not fitted")
        else:
            return self.weights.T
