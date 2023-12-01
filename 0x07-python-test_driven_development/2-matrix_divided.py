#!/usr/bin/python3
"""
This is module.
"""


def matrix_divided(matrix, div):
    """
    This is function.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) not in [int, float]:
                raise TypeError(msg)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x/div, 2), row)), matrix))
    return new_matrix
