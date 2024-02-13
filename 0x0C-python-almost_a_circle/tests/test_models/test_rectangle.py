#!/usr/bin/python3

"""
unittest for Rectangle class

# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_models/test_rectangle.py
"""


import os
import unittest
from io import StringIO
from contextlib import redirect_stdout
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for Rectangle class in models/rectangle.py"""

    def test_class(self):
        """ test instance created is rectangle class"""
        r = Rectangle(1, 2)
        self.assertEqual(type(r), Rectangle)

    def test_attr_match(self):
        """test that attribute match what is given"""
        r = Rectangle(12, 20, 1, 2, 10)
        self.assertTrue(r.width == 12)
        self.assertTrue(r.height == 20)
        self.assertTrue(r.x == 1)
        self.assertTrue(r.y == 2)
        self.assertTrue(r.id == 10)

    def test_default_attr(self):
        """Test default attributes are set when not given"""
        r2 = Rectangle(4, 8)
        self.assertTrue(r2.width == 4)
        self.assertTrue(r2.height == 8)
        self.assertTrue(r2.x == 0)
        self.assertTrue(r2.y == 0)
        self.assertTrue(r2.id is not None)

    def test_validate_attribute(self):
        """validate attributes"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("5", 4)
            Rectangle([1, 2], 4, 1, 1)
            Rectangle((1, 2), 4, 1, 1)
            Rectangle({1, 2}, 4, 1, 1)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)
            Rectangle(-2, 4, 1, 1)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "4")
            Rectangle(2, [1, 2])
            Rectangle(2, (1, 2), 1, 2)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
            Rectangle(2, -2, 1, 1)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "s", 1)
            Rectangle(4, 7, [1, 2], 2)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -1, 1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 1, "s")
            Rectangle(4, 7, 2, [1, 2])

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 1, -2)

    def test_invalid_args(self):
        """Test invalid args - too many or too little args"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7, 8)
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_area(self):
        """test the area method"""
        self.assertEqual(Rectangle(10, 20).area(), 200)
        self.assertEqual(Rectangle(7, 11, 1, 1).area(), 77)
        self.assertEqual(Rectangle(7, 11, 1, 1, 1).area(), 77)

    def test_display(self):
        """test the display method"""
        # Create a StringIO object to capture stdout
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(2, 3, 1, 1).display()
            self.assertEqual(buf.getvalue(), "\n ##\n ##\n ##\n")
        with StringIO() as buf, redirect_stdout(buf):
            Rectangle(4, 5).display()
            self.assertEqual(buf.getvalue(), "####\n####\n####\n####\n####\n")

    def test_print(self):
        """test the __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), '[Rectangle] (12) 2/1 - 4/6')

    def test_update(self):
        """test the update method"""
        """update with *args"""
        r = Rectangle(2, 2, 2, 2, 2)
        r.update()
        self.assertEqual(str(r), '[Rectangle] (2) 2/2 - 2/2')
        r.update(10)
        self.assertEqual(str(r), '[Rectangle] (10) 2/2 - 2/2')
        r.update(10, 8)
        self.assertEqual(str(r), '[Rectangle] (10) 2/2 - 8/2')
        r.update(10, 8, 12)
        self.assertEqual(str(r), '[Rectangle] (10) 2/2 - 8/12')
        r.update(10, 8, 12, 3)
        self.assertEqual(str(r), '[Rectangle] (10) 3/2 - 8/12')
        r.update(10, 8, 12, 3, 5)
        self.assertEqual(str(r), '[Rectangle] (10) 3/5 - 8/12')

        """update with *kwargs"""
        r.update(height=1)
        self.assertEqual(str(r), '[Rectangle] (10) 3/5 - 8/1')
        r.update(y=1, width=2, x=4, id=89)
        self.assertEqual(str(r), '[Rectangle] (89) 4/1 - 2/1')

        """Test update with invalid *args"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(10, 8, 12, 4, -5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(10, 8, 12, "4", 5)

        """Test update with invalid *kwargs"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(id=2, width="10", height=4, x=1, y=1)

        def test_dictionary(self):
            """Test the to_dictionary() method"""
            r1 = Rectangle(10, 2, 1, 9)
            r1_dictionary = r1.to_dictionary()
            self.assertEqual(type(r1_dictionary), dict)
            rstr = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
            self.assertEqual(r1_dictionary, rstr)
            r2 = Rectangle(1, 1)
            r2.update(**r1_dictionary)
            self.assertEqual(str(r2), '[Rectangle] (1) 1/9 - 10/2')
