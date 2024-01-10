#!/usr/bin/python3

'''computes the square value of all integers of a matrix'''


def square_matrix_simple(matrix=[]):
    result = []
    for list_item in matrix:
        result.append(list(map(lambda x: x*x, list_item)))
    return result
