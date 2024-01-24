#!/usr/bin/python3

"""
Module 102-square

Defines class Square with private instance attribute, size (with validation),
a public instance method, area, a property to retrieve(get) the size and a
property to set the size
"""


class Square:
    """
    class Square definition

    Attributes: size
    Methods: area
    properties to: get size, set size
    """

    def __init__(self, size=0):
        """
        Initializes a square with attribute size
        size defaults to 0 if none
        """

        self.size = size

    @property
    def size(self):
        """retrieve(get) size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set and validate size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate square area"""
        return (self.__size)**2

    def __eq__(self, other):
        """compares if two square areas are equal"""
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """compares two square areas not equal"""
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        """compares if a square greater than another"""
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """compares if a square greater than or equal to another"""
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        """compares if a square less than another"""
        if isinstance(other, Square):
            return self.area() < other.area()

    def __lt__(self, other):
        """compares if a square less than or equal to another"""
        if isinstance(other, Square):
            return self.area() <= other.area()
