#!/usr/bin/python3
"""
Module 103-magic_class

MagicClass definition
"""
import math


class MagicClass:
    """define MagicClass with methods"""
    def __init__(self, radius=0):
        """initialize MagicClass"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

        def area(self):
            """Calculate area"""
            return (self.__radius**2) * math.pi

        def circumference(self):
            """Calculate circumference"""
            return (2 * math.pi * self.__radius)


# import dis
# dis.dis(MagicClass)
