#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    number_of_instances = 0
    print_symbol = "#"

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        str = ""
        if (self.__height == 0) or (self.__width == 0):
            return ("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    if type(self.print_symbol) in [list, tuple, dict, int]:
                        str += repr(self.print_symbol)
                    else:
                        str += self.print_symbol
                if i < self.__height - 1:
                    str += "\n"
            return (str)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)
