#!/usr/bin/python3
"""Define  a  class BaseGeometry inherits class object"""


class BaseGeometry(object):
    """Represent a BaseGeometry class."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is int and greater than 0.
        Args:
            name:string name of int.
            value:int to verfy.
        Returns:
            Exception TypeError if type(value) not int
            or Exception ValueError if value <= 0.
            """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
