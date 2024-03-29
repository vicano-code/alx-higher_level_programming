#!/usr/bin/python3
"""
Module 2-Rectangle

Contains the Rectangle class with its attributes and methods

"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from Base

    Private Instance Attribute:
        width, height, x, y

    Methods:
        __init__(self, width, height, x=0, y=0, id=None)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
        x(self)
        x(self, value)
        y(self)
        y(self, value)
        area(self)
        display(self)
        __str__(self)
        update(self, *args, **kwargs)
        to_dictionary(self)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize instance attributes"""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

    @property
    def width(self):
        """get rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get coordinate x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set coordinate x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get coordinate y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set coordinate y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """compute area of rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """print rectangle representation to stdout"""
        print("\n" * self.__y + "\n".join([((" " * self.__x) +
              ("#" * self.__width)) for rows in range(self.__height)]))

    def __str__(self):
        """override the in-built str method"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """updates the Rectangle class attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.__width
        dic["height"] = self.__height
        dic["x"] = self.__x
        dic["y"] = self.__y
        return dic
