#!/usr/bin/python3
""" class Square that inherits from Rectangle
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Function initialize the attributes of the class

        Parameters
        ----------
        width : int
        width of Rectangle
        height : int
        height of Rectangle
        x : int

        y : int

        id : int
        id of Rectangle
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        """print the str of Rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Function that update Rectangle with value of args"""
        if len(args) != 0:
            for index in range(len(args)):
                if index == 0:
                    self.id = args[index]
                elif index == 1:
                    self.size = args[index]
                elif index == 2:
                    self.x = args[index]
                elif index == 3:
                    self.y = args[index]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
