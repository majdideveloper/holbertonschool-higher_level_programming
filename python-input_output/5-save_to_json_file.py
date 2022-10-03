#!/usr/bin/python3
"""This module  contains function that writes an Object to a text file,
using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Function function that writes an Object to a text file,
    using a JSON representation

    Parameters
    ----------
    my_obj : object(string)
        a JSON string
    filename : string
        name of file to writes in.

    """
    jsonStr = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(jsonStr)
    f.close()
