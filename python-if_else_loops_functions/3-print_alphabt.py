#!/usr/bin/python3
import sys
for char in range(97, 123):
    if char != 113 and char != 101:
        print("{}".format(chr(char)), end="")
