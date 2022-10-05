#!/usr/bin/python3
""" class Student
"""


class Student:
    """ My class Student
    """

    def __init__(self, first_name, last_name, age):
        """Function to initialize the attributes of the class.

        Args
        ----
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Parameters
        ----------
        attrs : list
        (Optional) The attributes to represent.
         """
        if attrs is None:
            return self.__dict__
        else:
            newDict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    newDict[attr]=self.__dict__[attr]
            return newDict





             
