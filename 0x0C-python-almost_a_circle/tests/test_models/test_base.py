#!/usr/bin/python3

"""
Module - unittest for Base class

# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_base.py
"""


import os
import unittest
import json
from io import StringIO
from contextlib import redirect_stdout
from models import base
from models import rectangle
Base = base.Base
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
        r = Rectangle(10, 7, 2, 8)
        dictionary = r.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(dictionary) == dict)
        self.assertTrue(type(json_dictionary) == str)
        self.assertTrue(json_dictionary, [{"x": 2, "width": 10,
                                           "id": 3, "height": 7, "y": 8}])

    def test_to_json_string_with_none(self):
        """to_json_string method test given its arg is None"""
        dic = None
        json_dic = Base.to_json_string([dic])
        self.assertTrue(type(json_dic) == str)
        self.assertTrue(json_dic, "[]")

    def test_to_json_string_with_empty_dict(self):
        """to_json_string method test given empty dict"""
        dic = dict()
        json_dic = Base.to_json_string(dic)
        self.assertTrue(len(dic) == 0)
        self.assertTrue(type(json_dic) == str)
        self.assertTrue(json_dic, "[]")

    def test_save_to_file(self):
        """save_to_file method test"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                    json.dumps([r1.to_dictionary(), r2.to_dictionary()]),
                    file.read())

    def test_save_to_file_with_no_instance(self):
        """save_to_file method test given no instance list"""
        r = None
        Rectangle.save_to_file(r)
        with open("Rectangle.json", "r") as file:
            self.assertTrue(file.read(), "[]")

    def test_save_to_file_with_empty_instance(self):
        """save_to_file method test given the arg is None"""
        r = []
        Rectangle.save_to_file(r)
        with open("Rectangle.json", "r") as file:
            self.assertTrue(file.read(), "[]")

    def test_from_json_string(self):
        """from_json_string method test"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(list_input) == list)
        self.assertTrue(type(json_list_input) == str)
        self.assertTrue(type(list_output) == list)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_with_none(self):
        """from_json_string method test with no json string of lists"""
        json_list_input = None
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)
        self.assertEqual(list_output, [])

    def test_from_json_string_with_empty_json_string(self):
        """from_json_string method test with empty json string of lists"""
        json_list_input = "[]"
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(list_output) == list)
        self.assertEqual(list_output, [])

    def test_create(self):
        """test the create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), '[Rectangle] (1) 1/0 - 3/5')
        self.assertEqual(str(r1), '[Rectangle] (1) 1/0 - 3/5')
        self.assertFalse(r1 == r2)
        self.assertIsNot(r1, r2)

    def test_load_from_file(self):
        """test the load_from_file method"""
        r3 = Rectangle(10, 7, 2, 8, 11)
        r4 = Rectangle(2, 4, 0, 0, 12)
        list_rectangles_input = [r3, r4]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_output), 2)
        for i, v in enumerate(list_rectangles_output):
            if i == 0:
                self.assertEqual(str(v), '[Rectangle] (11) 2/8 - 10/7')
            if i == 1:
                self.assertEqual(str(v), '[Rectangle] (12) 0/0 - 2/4')

    def test_load_from_none_file(self):
        """Test load from None file (file doe not exist"""
        Rectangle.save_to_file(None)
        rec = Rectangle.load_from_file()
        self.assertEqual(type(rec), list)
        self.assertEqual(len(rec), 0)

    def test_load_from_empty_file(self):
        """Test load from empty file"""
        Rectangle.save_to_file([])
        rec = Rectangle.load_from_file()
        self.assertEqual(type(rec), list)
        self.assertEqual(len(rec), 0)
