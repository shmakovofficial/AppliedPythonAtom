#!/usr/bin/env python
# coding: utf-8


import numpy as np
from ..metrics.metrics import *


class LogisticRegression:
    def __init__(
            self,
            lambda_coefficient=1.0,
            regularization=None,
            alpha=0.5,
            threshold=0.5,
            steps=1000,
            delta=0.1
    ):
        """
        LogReg for Binary case
        :param lambda_coefficient: constant coefficient for gradient descent step
        :param regularization: regularization type ("L1" or "L2") or None
        :param alpha: regularization coefficient
        :param threshold: decision threshold for classification
        :param steps: maximum steps for gradient descent
        :param delta: convergence criteria for gradient descent
        """
        self.step = lambda_coefficient
        self.weights = None
        self.tools = None
        self.threshold = threshold
        self.steps = steps
        self.delta = delta

        def grad_loss(y_true, x_train):
            y = x_train @ self.weights
            return -1 / y_true.shape[0] * \
                   (x_train *
                    (y_true /
                     (1 + np.exp(y)) +
                     (1 - y_true) /
                     (1 + np.exp(1 - y))
                     )
                    ).sum(axis=0).T

        if regularization == "L1":
            def loss_l1(y_true, y_pred):
                return logloss(y_true, y_pred) + \
                       alpha * np.abs(self.weights).sum()

            def grad_loss_l1(y_true, x_train):
                return grad_loss(y_true, x_train) + \
                       alpha * np.sign(self.weights)

            self.tools = loss_l1, grad_loss_l1
        elif regularization == "L2":
            def loss_l2(y_true, y_pred):
                return logloss(y_true, y_pred) + \
                       alpha * np.sqrt((self.weights ** 2).sum())

            def grad_loss_l2(y_true, x_train):
                return grad_loss(y_true, x_train) + \
                       alpha * 2 * self.weights

            self.tools = loss_l2, grad_loss_l2
        else:
            def loss(y_true, y_pred):
                return logloss(y_true, y_pred)

            self.tools = loss, grad_loss

    def fit(self, X_train, y_train):
        """
        Fit model using gradient descent method
        :param X_train: training data
        :param y_train: target values for training data
        :return: None
        """
        x = np.hstack(np.ones(y_train.shape), X_train)
        self.weights = np.ones((x, 1))
        count = 0
        prev_y = x @ self.weights
        while count < self.steps:
            self.weights -= self.step * self.tools[1](y_train, x)
            new_y = x @ self.weights
            if (new_y - prev_y) < self.delta:
                break
            prev_y = new_y
            count += 1

    def predict(self, X_test):
        """
        Predict using model.
        :param X_test: test data for predict in
        :return: y_test: predicted values
        """
        return self.predict_proba(X_test).apply(
            lambda i: 1 if i >= self.threshold else 0
        )

    def predict_proba(self, X_test):
        """
        Predict probability using model.
        :param X_test: test data for predict in
        :return: y_test: predicted probabilities
        """
        x = np.hstack(np.ones((X_test.shape[0], 1)), X_test)
        return 1 / (1 + np.exp(-x @ self.weights))

    def get_weights(self):
        """
        Get weights from fitted linear model
        :return: weights array
        """
        return self.weights
