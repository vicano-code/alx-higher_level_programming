#!/usr/bin/python3
"""
Module 9-rectangle

-Definition of a class 'Rectangle' with private attributes
width and height and public methods area and perimeter.
-returns a string representation of the rectangle to be able to
recreate a new instance by using eval()
-detects instance deletion
-calculates number of rectangle instances present
-string symbol stored in public class attribute print_symbol used as
symbol for the string representation of rectangle
-A static method to compare two rectangle instances
-A class method that returns a new rectangle instance which is a square
"""


class Rectangle:
    """
    defines Rectangle class with attributes width and height
    and methods

    parameters:
    width (int)
    height (int)

    class attributes:
    number_of_instances (int)
    print_symbol

    Methods:
    __init__(self, width=0, height=0)
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    area(self)
    perimeter(self)
    __str__(self)
    __repr__(self)
    __del__(self)
    bigger_or_equal(rect_1, rect_2)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """claculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints a string representation, # of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = "\n".join([str(self.print_symbol) * self.__width
                            for rows in range(self.__height)])
        return string

    def __repr__(self):
        """
        returns a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """detects instance deletion"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new rectangle instance which is a square"""
        return Rectangle(size, size)
