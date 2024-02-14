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
from models import square
Base = base.Base
Rectangle = rectangle.Rectangle
Square = square.Square


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

        Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 98)])
        saved_content = '[{"id": 98, "width": 1, "height": 2, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), saved_content)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertTrue(file.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertTrue(file.read(), [])

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([Square(1, 0, 0, 1)])
        result = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), result)

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

        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(str(s), '[Square] (89) 0/0 - 1')

        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s1), '[Square] (89) 2/0 - 1')

        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s1), '[Square] (89) 2/3 - 1')

    def test_load_from_file(self):
        """test the load_from_file method for Rectangle class"""
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

        """test the load_from_file method for Rectangle class"""
        Square.save_to_file([Square(2, 1, 3, 99)])
        sq = Square.load_from_file()
        self.assertEqual(len(sq), 1)
        self.assertEqual(str(sq[0]), '[Square] (99) 1/3 - 2')

        """Test load_from_file when file doesn't exist for Rectangle class"""
        Rectangle.save_to_file(None)
        rec = Rectangle.load_from_file()
        self.assertEqual(type(rec), list)
        self.assertEqual(len(rec), 0)

        """Test load_from_file(empty file) for Rectangle class"""
        Rectangle.save_to_file([])
        rec = Rectangle.load_from_file()
        self.assertEqual(type(rec), list)
        self.assertEqual(len(rec), 0)

        """Test load_from_file when file doesn't exist for Square class"""
        Square.save_to_file(None)
        sq = Square.load_from_file()
        self.assertEqual(type(sq), list)
        self.assertEqual(len(sq), 0)

        """Test load_from_file(empty file) for Square class"""
        Square.save_to_file([])
        sq = Square.load_from_file()
        self.assertEqual(type(sq), list)
        self.assertEqual(len(sq), 0)
