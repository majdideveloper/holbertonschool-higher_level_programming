#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    for item in my_list:
        if item > temp:
            temp = item
    return temp
