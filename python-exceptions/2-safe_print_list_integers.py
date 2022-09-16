#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_print = 0
    for idx in range(x):
        if x == idx:
            break
        if idx >= len(my_list):
            raise IndexError
        try:
            print("{:d}".format(my_list[idx]), end="")
            num_print += 1
        except (TypeError, ValueError):
            pass
    print()
    return num_print
