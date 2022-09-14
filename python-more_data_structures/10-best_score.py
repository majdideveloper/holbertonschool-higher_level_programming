#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best_value = 0
    list_val = list(a_dictionary.values())
    list_key = list(a_dictionary.keys())
    for value in list_val:
        if value > best_value:
            best_value = value
    position = list_val.index(best_value)
    return list_key[position]
