#!/usr/bin/python3
"""This module  contains  function that creates an Object from a “JSON file”"""

import sys

def class_to_json(obj):
    return obj.__dict__


