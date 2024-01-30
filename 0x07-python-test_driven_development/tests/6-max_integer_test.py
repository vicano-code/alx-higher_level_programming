#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """unit test of max_integer function"""
        
        # list is empty
        self.assertIsNone(max_integer(list=[]))

        # single value in list
        self.assertEqual(max_integer(list=[1]), 1)

        # several values in list
        list =  [1, 90, 2, 13, 34, 5, -13, 3]
        self.assertEqual(max_integer(list), 90)

        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

        list = [9, -1, 2, 3, 4, -30, 2]
        self.assertEqual(max_integer(list), 9)

        # 2 equal values in list
        list = [1, 1]
        self.assertEqual(max_integer(list), 1)

        # negative value list
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)


if __name__ == '__main__':
    unittest.main()
