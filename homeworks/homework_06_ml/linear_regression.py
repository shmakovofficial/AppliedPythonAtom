#!/usr/bin/env python
# coding: utf-8

import numpy as np
from metrics import mse


class LinearRegression:
    def __init__(self, lambda_coef=0.1, regulatization=None, alpha=0.1):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_step = lambda_coef
        self.fitted = False
        self.weights = None
        self.MAX_STEPS = 1000
        self.delta = 10 ** (-3)
        self.min_ = None
        self.max_ = None
        self.mean_ = None
        self.std_ = None
        if regulatization == "L1":
            def l1_loss(x, y):
                return (mse(y, x @ self.weights) +
                        alpha * np.abs(self.weights[1:]).sum())

            def l1_loss_grad(x, y):
                return (2 / y.shape[0] *
                        ((x @ self.weights - y).T @ x) +
                        alpha * np.sign(self.weights[1:])).reshape([-1, 1])

            self.tools = l1_loss, l1_loss_grad
        elif regulatization == "L2":
            def l2_loss(x, y):
                return (mse(y, x @ self.weights) +
                        alpha * np.linalg.norm(self.weights[1:].T))

            def l2_loss_grad(x, y):
                return (2 / y.shape[0] *
                        ((x @ self.weights - y).T @ x) +
                        alpha * 2 * self.weights[1:]).reshape([-1, 1])

            self.tools = l2_loss, l2_loss_grad
        else:
            def loss(x, y):
                return mse(y, x @ self.weights)

            def loss_grad(x, y):
                return 2 / y.shape[0] * \
                       ((x @ self.weights - y).T @ x).reshape([-1, 1])

            self.tools = loss, loss_grad

    def _calibrate_data(self, data, fit=True):
        # if fit:
        #    self.data_mean = data.mean()
        #    self.data_std = data.std()
        # x = (data - self.data_mean) / self.data_std
        # if fit:
        #    self.data_min = x.min()
        #    self.data_max = x.max()
        # x = (x - self.data_min) / (self.data_max - self.data_min)
        # return np.hstack((np.ones((x.shape[0], 1)), x))
        return np.hstack((np.ones((data.shape[0], 1)), data))

    def _calibrate_result(self, result):
        # result = result.reshape([-1, 1])
        # self.result_mean = result.mean()
        # self.result_std = result.std()
        # y = (result - self.result_mean) / self.result_std
        # self.result_min = y.min()
        # self.result_max = y.max()
        # y = (y - self.result_min) / (self.result_max - self.result_min)
        # return y
        return result

    def _expand_result(self, result):
        # return (result * (self.result_max - self.result_min) +
        #        self.result_min) * self.result_std + self.result_mean
        return result

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x = self._calibrate_data(X_train)
        y = self._calibrate_result(y_train)
        self.weights = np.ones((x.shape[1], 1))
        count = 0
        while count < self.MAX_STEPS:
            self.weights -= self.lambda_step * self.tools[1](x, y)
            if self.tools[0](x, y) < self.delta:
                break
            count += 1
        self.fitted = True

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        if not self.fitted:
            raise Exception("Model is not fitted")
        else:
            if X_test.shape[1] != self.weights.shape[0] - 1:
                raise Exception("Undefined")
            else:
                x = self._calibrate_data(X_test, fit=False)
                return self._expand_result(x @ self.weights)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if not self.fitted:
            raise Exception("Model is not fitted")
        else:
            return self.weights.T
