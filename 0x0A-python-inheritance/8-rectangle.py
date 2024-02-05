#!/usr/bin/python3

"""
Module 8-rectangle

Contains a class Rectangle that inherits from BaseGeometry in
7-base_geometry.py
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass with a parentclass

    Attributes:
    -width
    -height
    """

    def __init__(self, width, height):
        """Instantiation with attributes width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
