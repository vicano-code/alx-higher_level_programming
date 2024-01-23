#!/usr/bin/python3

"""
Module 2-square
Defines class Square with private instance attribute, size with validation
"""


class Square:
    """
    class Square definition

    Attributes:
        size
    """

    def __init__(self, size=0):
        """
        Initializes a square

        Attributes:
            size  - size of a side of a square defaulted to 0.
            size must be a positive integer
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
