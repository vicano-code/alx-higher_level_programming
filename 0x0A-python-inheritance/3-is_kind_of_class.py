#!/usr/bin/python3

"""
Module 3-is_kind_of_class

contains a function that returns True if the object is an
instance of, or if the object is an instance of a class that
inherited from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """check object instance"""
    return isinstance(obj, a_class)
