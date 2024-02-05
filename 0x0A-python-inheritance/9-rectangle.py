#!/usr/bin/python3

"""
Module 9-rectangle

Contains a class Rectangle that inherits from BaseGeometry in
7-base_geometry.py
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass with a superclass

    Attributes:
    -width
    -height

    Methods:
    -area(self)
    __str__(self)
    """

    def __init__(self, width, height):
        """Instantiation with attributes width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width,
                                              self.__height)
