#!/usr/bin/python3
"""Define  a  class MyInt"""


class MyInt(int):
    """Define a class MyInt inherited int"""
    def __init__(self, value):
        """Function Initialize."""
        int.__init__(self)
        self.value = value

    def __eq__(self, other):
        """Function inverse Equal."""
        return self.value != other

    def __ne__(self, other):
        """Function inverse Equal."""
        return self.value == other
