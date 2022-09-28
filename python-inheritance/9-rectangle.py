#!/usr/bin/python3
"""Define  a  class Rectangle inherited class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a Rectangle class inherited class BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new instance from Rectangle

        Args:
            width (int):The width of The new Rectangle
            height (int):The height oof The new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the Area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return String [Rectangle] width/height"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
