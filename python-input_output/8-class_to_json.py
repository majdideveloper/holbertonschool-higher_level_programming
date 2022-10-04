#!/usr/bin/python3
"""This module  contains function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean) for JSON
serialization of an object"""


def class_to_json(obj):
    """Function that creates an Object from a “JSON file”

    Parameters
    ----------
        obj : object
        any object
    """
    return obj.__dict__
