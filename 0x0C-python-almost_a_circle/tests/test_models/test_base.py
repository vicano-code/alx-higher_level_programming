#!/usr/bin/python3

"""
unittest for Base class

# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import base
Base = base.Base
from models import rectangle
Rectangle = rectangle.Rectangle


class TestBase(unittest.TestCase):
    """
    Base class tests
    """

    """Test attributes"""
    def test_id_given(self):
        """Test ids match"""
        self.assertTrue(Base(99), self.id == 99)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(-20), self.id == -20)

    def test_no_id_given(self):
        """Test ids match nb_objects increment when not given"""
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)

    def test_private_attr_access(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    """Test args given"""
    def test_invalid_args(self):
        """Test too many args given"""
        with self.assertRaises(TypeError):
            Base(10, 10)

    """Test class"""
    def test_class(self):
        """Test class created is indeed Base"""
        self.assertTrue(Base(10), self.__class__ == Base)

    def test_to_json_string(self):
        """to_json_string method test"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary) == dict)
        self.assertTrue(type(json_dictionary) == str)
        self.assertTrue(json_dictionary, [{"x": 2, "width": 10,
                                           "id": 3, "height": 7, "y": 8}])
