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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """ that prints in stdout the Rectangle """
        for line in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """print the str of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
             self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Function that update Rectangle with value of args"""
        if len(args) != 0:
            for index in range(len(args)):
                if index == 0:
                    self.id = args[index]
                elif index == 1:
                    self.__width = args[index]
                elif index == 2:
                    self.__height = args[index]
                elif index == 3:
                    self.__x = args[index]
                elif index == 4:
                    self.__y = args[index]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """funtion return dictionary of Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
