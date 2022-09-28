#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if obj is an inherited instance from the class.
     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is  an inherited instance of a_class - True.
        Otherwise - False.
    """

    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
