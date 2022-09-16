#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())
    list_values = list(a_dictionary.values())
    if value not in list_values:
        return a_dictionary
    for index in range(len(list_values)):
        if list_values[index] == value:
            a_dictionary.pop(list_keys[index])
    return a_dictionary
