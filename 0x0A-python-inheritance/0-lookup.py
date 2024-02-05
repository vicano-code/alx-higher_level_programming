#!/usr/bin/python3

"""
Module 0-Lookup
Returning the list of available attributes and methods of an object
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
