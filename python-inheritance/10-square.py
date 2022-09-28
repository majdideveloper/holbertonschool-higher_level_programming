#!/usr/bin/python3
"""Define  a  class Square inherited class Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Rectangle class inherited class BaseGeometry."""

    def __init__(self, size):
        """Intialize a new instance from Square

        Args:
            size (int):The size of The new Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Intialize a new instance from Square"""
        return self.__size * self.__size

    def __str__(self):
        """Return String [Rectangle] size/size"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
