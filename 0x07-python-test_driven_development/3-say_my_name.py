#!/usr/bin/python3
"""
Module 3-say_my_name

-function that prints My name is <first name> <last name>
-first_name and last_name must be strings
"""


def say_my_name(first_name, last_name=""):
    """prints My name is <first name> <last name>"""

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
