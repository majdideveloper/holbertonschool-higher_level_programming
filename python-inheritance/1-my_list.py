#!/usr/bin/python3
"""Defines an class MyList."""


class MyList(list):
    """Defines an class MyList."""

    def __init__(self):
        """function Initialize."""
        list.__init__(self)

    def print_sorted(self):
        """Return sorted list."""
        print(sorted(self))
