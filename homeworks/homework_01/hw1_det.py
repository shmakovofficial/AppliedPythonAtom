#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    for i in list_of_lists:
        if len(i) is not len(list_of_lists):
            return None

    def add_matrix(matrix, el_x, el_y):
        # print("Addmatrix from: ", matrix, "w/: ", el_x, "::", el_y)
        new_matrix = [j.copy() for j in matrix]
        for j in new_matrix:
            j.pop(el_y)
        new_matrix.pop(el_x)
        # print("Result is: ", new_matrix)
        return new_matrix

    def calc_det(matrix):
        if len(matrix) < 2:
            return matrix[0][0]
        else:
            result = 0
            sign = -1
            for j in range(len(matrix)):
                sign *= -1
                # print("The sign is now: ", sign)
                result += (matrix[0][j] *
                           calc_det(add_matrix(matrix, 0, j)) * sign)
                # print("Result changed to: ", result)
            return result

    return calc_det(list_of_lists)
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
