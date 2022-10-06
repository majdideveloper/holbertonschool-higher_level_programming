#!/usr/bin/python3
""" class Base
"""

import json


class Base:
    """class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Function that creates an Object from a “JSON file”

        Parameters
        ----------
        id : int
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """update the class Base by adding the static method
        def to_json_string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
