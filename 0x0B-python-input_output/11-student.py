#!/usr/bin/python3
"""
Module 11-student.py

-Contains a class Student that defines a student with attributes
first_name, last_name, age; and method to_json(self, attrs=None)
retrieves a dictionary representation of a Student instance
-If attrs is a list of strings, only attribute names contained
in this list must be retrieved Otherwise, all attributes must be
retrieved.
-With public method reload_from_json(self, json): that replaces
all attributes of the Student instance
"""


class Student:
    """
    Attributes:
    -first_name
    -last_name
    -age

    Methods:
    - to_json(self, attrs=None): retrieves a dict representation
    of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """initialize attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of a Student instance"""
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    new_dict.update({i: self.__dict__[i]})
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
