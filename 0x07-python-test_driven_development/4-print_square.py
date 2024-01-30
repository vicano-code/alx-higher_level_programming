#!/usr/bin/python3
"""
Module 4-print_square

-function that prints a square with the character #
-size must be an integer and > 0
"""


def print_square(size):
    """prints a square with the character #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    print("\n".join(["#"*size for i in range(size)]))
