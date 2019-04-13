#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    if not derivative:
        return ((y_true - y_hat) ** 2).mean()
    else:
        return ((2 * (y_true - y_hat) - ((y_true - y_hat) ** 2).mean()) /
                y_true.shape[0])


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return (np.absolute(y_true - y_hat)).mean()


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    return 1 - mse(y_true, y_hat) / mse(y_true, y_true.mean())
