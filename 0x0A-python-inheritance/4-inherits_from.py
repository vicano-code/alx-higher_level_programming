#!/usr/bin/python3
"""
Module 4-inherits_from

Contains  a function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
from the specified class, otherwise False
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Notes:
    -use type() to get specific class
    -use isinstance() to get class and any parent classes too
    -use issubclass() to get what object is a subclass of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
