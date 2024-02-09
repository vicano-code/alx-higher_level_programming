#!/usr/bin/python3
"""
Module Square


"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square attributes from superclass rectangle"""
        super().__init__(size, size, x, y, id)
        self.__size = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """override the in-built str method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                self.id, self.__x, self.__y, self.__size)

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set square size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """updates the square attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__size = args[1]
            if len(args) >= 3:
                self.__x = args[2]
            if len(args) == 4:
                self.__y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.__size = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.__size
        dic["x"] = self.__x
        dic["y"] = self.__y
        return dic
