#!/usr/bin/python3
"""Function say_my_name """


def say_my_name(first_name, last_name=""):
    """Function say_my_name and return string."""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if first_name is "":
        return None

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
