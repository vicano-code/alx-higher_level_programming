#!/usr/bin/python3

"""
Module 100-my_int

Contains  a class MyInt that inherits from int
MyInt has == and != operators inverted
"""


class MyInt(int):
    """ a class MyInt that inherits from int"""

    def __init__(self, val):
        """initialize val"""
        self.val = val

    def __eq__(self, other):
        """return false if val is type int and vice versa"""
        return self.val != other

    def __ne__(self, other):
        """return false if val not equal to int"""
        return self.val == other
