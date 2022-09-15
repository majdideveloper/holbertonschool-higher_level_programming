#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(0, int(x)):
        try:
            print(f"{my_list[i]}", end="")
            if i == x - 1:
                print("")
        except IndexError:
            print("")
            return i
    return i + 1
