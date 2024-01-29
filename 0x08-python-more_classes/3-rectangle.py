#!/usr/bin/python3
"""
Module 3-rectangle

-Definition of a class 'Rectangle' with private attributes
width and height and public methods area and perimeter with
-returns a string representation of the rectangle
"""


class Rectangle:
    """
    defines Rectiangle class with attributes width and height
    and methods

    parameters:
    width (int)
    height (int)

    Methods:
    __init__(self, width=0, height=0)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    area(self)
    perimeter(self)
    __str__(self)
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

    def area(self):
        """calculate area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """claculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string representation, # of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = "\n".join(["#" * self.__width
                            for rows in range(self.__height)])
        return string
