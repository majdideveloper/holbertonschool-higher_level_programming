#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_keys = list(a_dictionary.keys())
    list_keys.sort()
    for key in list_keys:
        print(f'{key}: {a_dictionary[key]}')
