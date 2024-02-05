#!/usr/bin/python3

"""
Module 11-square

Contains a class Square that inherits from class Rectangle in
9-rectangle.py
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A subclass, Square with a superclass, Rectangle

    Attributes:
    -size

    Methods:
    -__init__(self, size)
    - __str__(self)
    """

    def __init__(self, size):
        """initialize size"""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
