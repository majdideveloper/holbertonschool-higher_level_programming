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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that write the JSON string to file
        """
        fileName = cls.__name__ + ".json"
        list_dic = []
        with open (fileName, "w") as jsonFile:
            if list_objs is None:
                jsonFile.write(list_dic)
            else:
                for obj in list_objs:
                    list_dic.append(obj.to_dictionary())
                jsonFile.write(cls.to_json_string(list_dic))
