#!/usr/bin/env python
# coding: utf-8


import numpy as np

THRESHOLD = 0.5


def estimate(y_pred, threshold=THRESHOLD):
    """
        class decision
        :param y_pred: vector of estimated probabilities
        :param threshold: classification threshold
        :return: vector of estimated class values
        """

    def decision(t):
        if t >= threshold:
            return 1
        else:
            return 0

    decide = np.vectorize(decision)
    return decide(y_pred)


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated probabilities
    :return: loss
    """
    return (-1 / y_true.shape[0] *
            (y_true * np.log(y_pred) +
             (1 - y_true) * np.log(1 - y_pred)
             ).sum())


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: accuracy
    """
    return y_true[y_true == y_pred].shape[0] / y_true.shape[0]


def precision(y_true, y_pred):
    """
    precision
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: precision
    """
    return (y_pred[(y_pred == y_true) & (y_true == 1)].shape[0] /
            y_pred[y_pred == 1].shape[0])


def recall(y_true, y_pred):
    """
    recall
    :param y_true: vector of truth (correct) class values
    :param y_pred: vector of estimated class values
    :return: recall
    """
    return (y_pred[(y_pred == y_true) & (y_true == 1)].shape[0] /
            y_true[y_true == 1].shape[0])


def false_recall(y_true, y_pred):
    """
        false_recal
        :param y_true: vector of truth (correct) class values
        :param y_pred: vector of estimated class values
        :return: false_recall
        """
    return (y_pred[(y_pred == 1) & (y_true == 0)].shape[0] /
            y_true[y_true == 0].shape[0])


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_pred: vector of estimated probabilities
    :return: roc_auc
    """
    data = dict()
    for threshold in np.linspace(0, 1):
        data[false_recall(y_true, estimate(y_pred, threshold))] = \
            recall(y_true, estimate(y_pred, threshold))
    x_data = sorted([i for i in data.keys()])
    y_data = [data[i] for i in x_data]
    return np.trapz(y_data, x=x_data)
