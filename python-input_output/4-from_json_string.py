#!/usr/bin/python3
"""This module  contains function that returns an object
(Python data structure) represented by a JSON string"""


import json


def from_json_string(my_obj):
    """Function that returns an object (Python data structure)
    represented by a JSON string

    Parameters
    ----------
    my_obj : object(string)
        a JSON string

    Returns
    -------
    object
        object (Python data structure)
   """
    objFromJson = json.loads(my_obj)
    return objFromJson
