#!/usr/bin/python3
import sys
for num in range(0, 100):
    if num == 99:
        print("{:02d}".format(num))
        break
    print("{:02d}, ".format(num), end="")
