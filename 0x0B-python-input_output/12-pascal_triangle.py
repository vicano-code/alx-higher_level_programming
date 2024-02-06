#!/usr/bin/python3
"""
Module 12-pascal_triangle.py

**Interview Prep**
-Contains a function def pascal_triangle(n): that returns
a list of lists of integers representing the Pascal’s triangle of n
-Returns an empty list if n <= 0
"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    m = [[1]]
    i = 2
    while i < n + 1:
        j = 1
        k = [1]
        while j < i:
            try:
                k.append(m[-1][j-1] + m[-1][j])
            except IndexError:
                k.append(m[-1][j-1])
            j += 1
        m.append(k)
        i += 1
    return m
