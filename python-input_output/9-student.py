#!/usr/bin/python3
""" class Student
"""

class Student:
    """ My class Student
    """

    def __init__(self, first_name, last_name, age):
        """Function to initialize the attributes of the class.
        """ 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that creates an Object from a “JSON file”

        Parameters
        ----------
        obj : object
        any object
         """
        return self.__dict__
