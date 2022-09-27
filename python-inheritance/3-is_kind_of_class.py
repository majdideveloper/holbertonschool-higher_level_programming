#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if obj is instance from the class.
     Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is  an instance of a_class - True.
        Otherwise - False.
    """
    return isinstance(obj, a_class)
