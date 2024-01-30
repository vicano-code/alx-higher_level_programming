#!/usr/bin/python3
"""
Module 2-matrix_divided

a function that divides all elements of a matrix
-matrix must be a list of lists of integers or floats
-Each row of the matrix must be of the same size
-divisor must be an integer and must not be 0
"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix"""

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for row in matrix:
        new_list.append(list(map(lambda x: round(x/div, 2), row)))
    return new_list
