#!/usr/bin/python3
"""This module  contains function that returns the JSON representation
of an object (string)"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)

    Parameters
    ----------
    my_obj : object(string)
        object to representation in JSON string

    Returns
    -------
    string
        the JSON representation of an object
   """
    json.dumps(my_obj)
