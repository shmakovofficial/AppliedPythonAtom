#!/usr/bin/env python
# coding: utf-8

import numpy as np


class LinearRegression:
    def __init__(self, lambda_coef=1.0, regulatization=None, alpha=0.5):
        """
        :param lambda_coef: constant coef for gradient descent step
        :param regulatization: regularizarion type ("L1" or "L2") or None
        :param alpha: regularizarion coefficent
        """
        self.lambda_step = lambda_coef
        self.fitted = False
        self.weights = None
        self.MAX_STEPS = 10
        self.delta = 10 ** (-3)
        self.min_ = None
        self.max_ = None
        self.mean_ = None
        self.std_ = None
        if regulatization == "L1":
            def l1_loss(x, y):
                return ((y - x @ self.weights).T
                        @ (y - x @ self.weights)) \
                       / self.weights.shape[0] \
                       + alpha * np.abs(self.weights[1:]).sum()

            def l1_loss_grad(x, y):
                return (2 / self.weights.shape[0] *
                        (x @ self.weights - y).T * x +
                        alpha * np.sign(self.weights[1:])).T

            self.tools = l1_loss, l1_loss_grad
        elif regulatization == "L2":
            def l2_loss(x, y):
                return ((y - x @ self.weights).T
                        @ (y - x @ self.weights)) \
                       / self.weights.shape[0] \
                       + alpha * np.linalg.norm(self.weights[1:])

            def l2_loss_grad(x, y):
                return (2 / self.weights.shape[0] *
                        (x @ self.weights - y).T * x +
                        alpha * 2 * self.weights[1:].T).T

            self.tools = l2_loss, l2_loss_grad
        else:
            def loss(x, y):
                return ((y - x @ self.weights).T
                        @ (y - x @ self.weights)) \
                       / self.weights.shape[0]

            def loss_grad(x, y):
                return (2 / self.weights.shape[0] *
                        (x @ self.weights - y).T * x).T

            self.tools = loss, loss_grad

    def _calibrate(self, data):
        x = (data - self.mean_) / self.std_
        x = (data - self.min_) / (self.max_ - self.min_)
        return x

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        self.mean_ = X_train.mean()
        self.std_ = X_train.std()
        self.min_ = X_train.min()
        self.max_ = X_train.max()
        x = self._calibrate(X_train)
        x = np.hstack((np.ones((X_train.shape[0], 1)), X_train))
        self.weights = np.ones((x.shape[1], 1))
        count = 0
        prev_result = 0
        while count < self.MAX_STEPS:
            result = self.tools[0](X_train, y_train)
            self.weights -= self.lambda_step * self.tools[1](X_train, y_train)
            if count == 0:
                prev_result = result
            else:
                if prev_result - result < self.delta:
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
                x = self._calibrate(X_test)
                return (np.hstack((np.ones((x.shape[0], 1)), x)) @
                        self.weights)

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if not self.fitted:
            raise Exception("Model is not fitted")
        else:
            return self.weights.reshape((1, -1))
