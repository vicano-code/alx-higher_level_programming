#!/usr/bin/python3
"""
Module 5-square

Defines class Square with private instance attribute, size (with validation),
a public instance method, area, a property to retrieve(get) the size and a
property to set the size, and a public method that prints in stdout the
square with the character #
"""


class Square:
    """
    class Square definition

    Attributes: size
    Methods: area, my_print
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
        """
        retrieve(get) size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set and validate size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate square area
        """
        return (self.__size)**2

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        print("\n".join(["#" * self.__size for rows in range(self.__size)]))
