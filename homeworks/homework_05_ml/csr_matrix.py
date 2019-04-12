#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix
    """

    def __init__(self, init_matrix_representation):
        """
        :param init_matrix_representation: can be usual dense matrix
        or
        (row_ind, col, data) tuple with np.arrays,
            where data, row_ind and col_ind satisfy the relationship:
            a[row_ind[k], col_ind[k]] = data[k]
        """
        if (isinstance(init_matrix_representation, tuple) and
                len(init_matrix_representation) == 3):
            self.A = np.zeros(len(init_matrix_representation[2]))
            self.IA = np.zeros(
                max(init_matrix_representation[0]) + 2,
                dtype=int
            )
            self.JA = np.zeros(
                len(init_matrix_representation[2]),
                dtype=int
            )
            self.size = max(init_matrix_representation[1]) + 1
            arr = sorted(list(zip(*init_matrix_representation)))
            for i, j in enumerate(arr):
                self.A[i], self.JA[i] = j[2], j[1]
                self.IA[j[0] + 1] += 1
            for i in range(self.IA.shape[0] - 1):
                self.IA[i + 1] += self.IA[i]
        elif isinstance(init_matrix_representation, np.ndarray):
            self.A = np.array([])
            self.IA = np.zeros(
                init_matrix_representation.shape[0] + 2,
                dtype=int
            )
            self.JA = np.array([], dtype=int)
            self.size = init_matrix_representation.shape[1]
            for i, x in enumerate(init_matrix_representation):
                for j, y in enumerate(x):
                    if y != 0:
                        self.A = np.append(self.A, y)
                        self.JA = np.append(self.JA, j)
                        self.IA[i + 1] += 1
            for i in range(self.IA.shape[0] - 1):
                self.IA[i + 1] += self.IA[i]
        else:
            raise ValueError

    def get_item(self, i, j):
        """
        Return value in i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if i >= self.IA.shape[0] - 1 or i < 0 or j < 0 or j >= self.size:
            raise IndexError
        else:
            for k in range(self.IA[i], self.IA[i + 1]):
                if self.JA[k] == j:
                    return self.A[k]
            return 0

    def set_item(self, i, j, value):
        """
        Set the value to i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        if i >= self.IA.shape[0] - 1 or i < 0 or j < 0 or j >= self.size:
            raise IndexError
        else:
            for k in range(self.IA[i], self.IA[i + 1]):
                if self.JA[k] > j:
                    self.JA = np.insert(self.JA, k, j)
                    self.A = np.insert(self.A, k, value)
                    for t in range(i + 1, self.IA.shape[0]):
                        self.IA[t] += 1
                    return
                if self.JA[k] == j:
                    self.A[k] = value
                    return
            if j > self.JA.shape[0] - 1:
                self.JA = np.append(self.JA, j)
                self.A = np.append(self.A, value)
                for t in range(i + 1, self.IA.shape[0]):
                    self.IA[t] += 1
                return
            self.JA = np.insert(self.JA, self.IA[i + 1], j)
            self.A = np.insert(self.A, self.IA[i + 1], value)
            for k in range(i + 1, self.IA.shape[0]):
                self.IA[k] += 1

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        matrix = np.zeros((self.IA.shape[0] - 1, self.size))
        for i in range(0, self.IA.shape[0] - 2):
            for j in range(self.IA[i], self.IA[i + 1]):
                matrix[i][self.JA[j]] = self.A[j]
        return matrix
