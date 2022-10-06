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
        with open(fileName, "w") as jsonFile:
            if list_objs is None:
                jsonFile.write(cls.to_json_string(list_dic))
            else:
                for obj in list_objs:
                    list_dic.append(obj.to_dictionary())
                jsonFile.write(cls.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """method that write the list of the JSON from json string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    """
    Dictionary to Instance
    """
    @classmethod
    def create(cls, **dictionary):
        """
        method that returns an instance with
        all attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    """
    File to instances
    """
    @classmethod
    def load_from_file(cls):
        """
        that returns a list of instances:
        """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as f:
                lis_obj = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in lis_obj]
        except FileNotFoundError:
            return []
