#!/usr/bin/python3
"""
Module 9-student.py

-Contains a class Student that defines a student
"""


class Student:
    """
    Attributes:
    -first_name
    -last_name
    -age

    Methods:
    - to_json(self): retrieves a dict representation
    of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation of a Student instance"""
        return self.__dict__
