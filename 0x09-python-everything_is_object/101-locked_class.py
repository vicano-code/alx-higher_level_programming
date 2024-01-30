#!/usr/bin/python3
"""
Module 101-locked class

Dynamically control attribute instance creation
"""


class LockedClass:
    """
    A class with no class or object attribute, that prevents
    the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name

    >>> a = LockedClass()
    >>> a.first_name = 'Victor'
    >>> a.first_name
    'Victor'

    >>> a.last_name = 'Berry'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """

    __slots__ = "first_name"
