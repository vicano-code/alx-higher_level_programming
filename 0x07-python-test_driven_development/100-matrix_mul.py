#!/usr/bin/python3
"""
Module 100-Matrix Multiplication
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("{} must be a list".format
                        ("m_a" if not isinstance(m_a, list) else "m_b"))

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for my_list in m_a:
        if not isinstance(my_list, list):
            raise TypeError("m_a must be a list of lists")
        for val in my_list:
            if not isinstance(val, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(my_list) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for my_list in m_b:
        if not isinstance(my_list, list):
            raise TypeError("m_b must be a list of lists")
        for val in my_list:
            if not isinstance(val, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(my_list) != len(m_a[0]):
            raise TypeError("each row of m_b must be of the same size")
        if len(my_list) != len(m_a) or len(m_b) != len(m_a[0]):
            raise ValueError("m_a and m_b can't be multiplied")

    result = []
