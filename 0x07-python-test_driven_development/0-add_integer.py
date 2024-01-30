#!/usr/bin/python3
"""
Module 0-add_integer

A function that adds two integers
"""


def add_integer(a, b=98):
    """
    Add two integers

    Parameters:
    - a (int or float), if float cast to int
    - b (int or float), if float cast to int

    Return:
    - integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
