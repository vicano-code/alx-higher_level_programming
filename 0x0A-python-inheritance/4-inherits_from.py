#!/usr/bin/python3
"""
Module 4-inherits_from.py

Contains  a function that returns True if the object is an
instance of a class that inherited (directly or indirectly)
frm the specified class, otherwise False
"""


def inherits_from(obj, a_class):
    """
    checks if an object is an instance of a class that inherited
    (directly or indirectly) frm the specified class
    """
    return type(obj) is not a_class and issubclass(type(obj), a_class)
