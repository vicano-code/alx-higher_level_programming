#!/usr/bin/python3

"""
Module 7-base_geometry

Contains a class BaseGeometry
-with Public instance method, area(self) that raises an Exception
-and public instance method integer_validator that validates value
"""


class BaseGeometry:
    """
    Methods:
    -area(self)
    -integer_validator(self, name, value)
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
