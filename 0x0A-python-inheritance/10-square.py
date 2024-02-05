#!/usr/bin/python3

"""
Module 10-square

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
    -and inherits super class methods
    """

    def __init__(self, size):
        """initialize size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
