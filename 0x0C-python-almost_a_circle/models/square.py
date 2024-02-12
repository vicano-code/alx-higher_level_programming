#!/usr/bin/python3
"""
Module Square

Inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square with methods
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initialize square attributes from superclass rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set square size as width and height"""
        self.width = value
        self.height = value

    def __str__(self):
        """override the in-built str method"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.x,
                self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the square attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
