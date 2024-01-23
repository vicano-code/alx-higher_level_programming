#!/usr/bin/python3

"""
Module 3-square

Defines class Square with private instance attribute, size (with validation)
and a public instance method, area.
"""


class Square:
    """
    class Square definition

    Attributes: size
    Methods: area
    """

    def __init__(self, size=0):
        """
        Initializes a square with attribute size
        size defaults to 0 if none
        validates size
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculate square area
        """
        return (self.__size ** 2)
