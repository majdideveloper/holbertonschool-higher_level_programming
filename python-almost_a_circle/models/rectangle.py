#!/usr/bin/python3
""" class Rectangle that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
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
        id = super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
