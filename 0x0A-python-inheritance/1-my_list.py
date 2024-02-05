#!/usr/bin/python3

"""
Module 1-my_list

Contains a class MyList that inherits from list and
Public instance method: def print_sorted(self): that
prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """
    A class that inherits from list
    """
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
