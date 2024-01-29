#!/usr/bin/python3
"""
Module 1-rectangle

Definition of a class 'Rectangle' with private attributes
and methods

"""


class Rectangle:
    """
    defines Rectangle class with attributes width and height

    parameters:
    width (int)
    height (int)

    Methods:
    __init__(self, width=0, height=0)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    """
    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
