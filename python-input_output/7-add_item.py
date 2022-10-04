#!/usr/bin/python3
"""This module  contains  function that creates an Object from a “JSON file”"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
arg = sys.argv[1:]

if len(sys.argv) == 1:
    myList = []
else:
    myList = load_from_json_file(filename)
myList.extend(arg)
save_to_json_file(myList, filename)
