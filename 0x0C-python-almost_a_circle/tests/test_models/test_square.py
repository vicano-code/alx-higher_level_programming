#!/usr/bin/python3

"""
unittest for Square class

# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import square
Square = square.Square


class TestSquare(unittest.TestCase):
    """Tests for Rectangle class in models/rectangle.py"""

    def test_class(self):
        """ test instance created is rectangle class"""
        s = Square(1)
        self.assertEqual(type(s), Square)

    def test_attr_match(self):
        """test that attribute match what is given"""
        s = Square(12, 1, 2, 10)
        self.assertTrue(s.width == 12)
        self.assertTrue(s.height == 12)
        self.assertTrue(s.x == 1)
        self.assertTrue(s.y == 2)
        self.assertTrue(s.id == 10)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        s = Square(4)
        self.assertTrue(s.width == 4)
        self.assertTrue(s.height == 4)
        self.assertTrue(s.x == 0)
        self.assertTrue(s.y == 0)
        self.assertTrue(s.id is not None)

    def test_validate_attribute(self):
        """validate attributes"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
            Square([1, 2], 1, 1)
            Square((1,), 1, 1)
            Square({"s", 2})

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
            Square(-1)
            Square(-2, 1, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "s", 1)
            Square(4, [1, 2], 2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -1, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(4, 1, "s")
            Square(4, 2, [1, 2])

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 4, -2)

    def test_invalid_args(self):
        """Test invalid args - too many or too little args"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_area(self):
        """test the area method"""
        self.assertEqual(Square(10).area(), 100)
        self.assertEqual(Square(7, 1, 1).area(), 49)

    def test_display(self):
        """test the display method"""
        # Create a StringIO object to capture stdout
        with StringIO() as buf, redirect_stdout(buf):
            Square(2, 1, 1).display()
            self.assertEqual(buf.getvalue(), "\n ##\n ##\n")
        with StringIO() as buf, redirect_stdout(buf):
            Square(4).display()
            self.assertEqual(buf.getvalue(), "####\n####\n####\n####\n")

    def test_print(self):
        """test the __str__ method"""
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), '[Square] (12) 2/1 - 4')

    def test_update(self):
        """test the update method"""
        """update with *args"""
        s = Square(2, 2, 2, 2)
        s.update()
        self.assertEqual(str(s), '[Square] (2) 2/2 - 2')
        s.update(10)
        self.assertEqual(str(s), '[Square] (10) 2/2 - 2')
        s.update(10, 8)
        self.assertEqual(str(s), '[Square] (10) 2/2 - 8')
        s.update(10, 8, 3, 5)
        self.assertEqual(str(s), '[Square] (10) 3/5 - 8')

        """update with *kwargs"""
        s.update(size=10)
        self.assertEqual(str(s), '[Square] (10) 3/5 - 10')
        s.update(y=1, size=2, x=4, id=89)
        self.assertEqual(str(s), '[Square] (89) 4/1 - 2')

        """Test update with invalid *args"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(10, 8, 4, -5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(10, 8, "4", 5)

        """Test update with invalid *kwargs"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(id=2, size="10", x=1, y=1)

        def test_dictionary(self):
            """Test the to_dictionary() method"""
            s = Square(10, 1, 9, 1)
            s_dictionary = s.to_dictionary()
            self.assertEqual(type(s_dictionary), dict)
            s_dict = {'x': 1, 'y': 9, 'id': 1, 'size': 10}
            self.assertEqual(s_dictionary, s_dict)
            s1 = Square(1)
            s1.update(**s_dictionary)
            self.assertEqual(str(s1), '[Square] (1) 1/9 - 10')
