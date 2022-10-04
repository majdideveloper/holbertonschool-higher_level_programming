#!/usr/bin/python3
"""This module  contains  function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file”

    Parameters
    ----------
        filename : filename
        “JSON file”
    Returns
    -------
    object
        object (Python data structure)
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        objFromJson = json.loads(read_data)
        return objFromJson
