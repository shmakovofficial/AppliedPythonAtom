#!/usr/bin/env python
# coding: utf-8


import numpy as np
import sys
from metrics import *

sys.path.append('../metrics')


class LogisticRegression:
    def __init__(self, lambda_coefficient=1.0, regularization=None,
                 alpha=0.5, threshold=0.5, n_iter=1000, delta=0.5):
        """
        LogReg for Binary case
        :param lambda_coefficient: constant coefficient for gradient descent step
        :param regularization: regularization type ("L1" or "L2") or None
        :param alpha: regularization coefficient
        :param threshold: decision threshold for classification
        :param n_iter: maximum steps for gradient descent
        :param delta: convergence criteria for gradient descent
        """
        self.lambda_coefficient = lambda_coefficient
        self.weights = None
        self.threshold = threshold
        self.n_iter = n_iter
        self.delta = delta
        self.fitted = False
        self.regularization = regularization
        self.alpha = alpha

    def _logloss_grad(self, y_true, x_train):
        y = x_train @ self.weights
        return (-1 / y_true.shape[0] *
                (x_train *
                 (y_true / (1 + np.exp(y)) -
                  (1 - y_true) / (1 + np.exp(1 - y)))
                 )).sum(axis=0)

    def _loss(self, y_true, y_pred):
        if self.regularization == "L1":
            return (logloss(y_true, y_pred) +
                    self.alpha * np.linalg.norm(self.weights[1:], ord=1))
        elif self.regularization == "L2":
            return (logloss(y_true, y_pred) +
                    self.alpha * np.linalg.norm(self.weights[1:]))
        else:
            return logloss(y_true, y_pred)

    def _loss_grad(self, y_true, x_train):
        if self.regularization == "L1":
            return (self._logloss_grad(y_true, x_train) +
                    self.alpha * np.sign(np.vstack((0, self.weights[1:])).T))
        elif self.regularization == "L2":
            return ((self._logloss_grad(y_true, x_train) +
                     self.alpha / np.linalg.norm(self.weights[1:].T)) *
                    np.vstack((0, self.weights[1:])).T)
        else:
            return self._logloss_grad(y_true, x_train)

    def fit(self, x_train, y_train):
        """
        Fit model using gradient descent method
        :param x_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x = np.hstack((np.ones((y_train.shape[0], 1)), x_train))
        self.weights = np.ones((x.shape[1], 1))
        count = 0
        while count < self.n_iter:
            self.weights -= self.lambda_coefficient * \
                            self._loss_grad(y_train, x).reshape((-1, 1))
            if (self._loss(y_train, 1 / (1 + np.exp(-(x @ self.weights)))) <
                    self.delta):
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
            raise ValueError

        return estimate(self.predict_proba(X_test), threshold=self.threshold)

    def predict_proba(self, x_test):
        """
        Predict probability using model.
        :param x_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        if not self.fitted:
            raise ValueError

        x = np.hstack((np.ones((x_test.shape[0], 1)), x_test))
        return 1 / (1 + np.exp(-(x @ self.weights)))

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        if not self.fitted:
            raise ValueError
        return self.weights
