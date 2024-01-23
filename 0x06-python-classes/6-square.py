#!/usr/bin/python3
"""
Module 6-square

Defines class Square with private instance attribute, size (with validation),
private instance attribute, position(with validation), a public instance
method, area, a property to retrieve(get) the size and a
property to set the size, and a public method that prints in stdout the
square with the character # and the position with spaces
"""


class Square:
    """
    class Square definition

    Attributes: size, position
    Methods: area, my_print
    properties to: get size, set size, get positiion, set position
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with attribute size
        size defaults to 0 if none
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        retrieve(get) square position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set and validate position
        """

        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculate square area
        """
        return (self.__size)**2

    def my_print(self):
        """
        prints in stdout the square with the character # and the
        position with spaces
        """
        print("\n" * self.__position[1], end="")
        print("\n".join([" " * self.__position[0] +
                         "#" * self.__size for rows in range(self.__size)]))
