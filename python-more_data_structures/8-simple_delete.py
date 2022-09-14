#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    list_keys = list(a_dictionary.keys())
    if key in list_keys:
        del a_dictionary[key]
        return a_dictionary
    return a_dictionary
