#!/usr/bin/python3
a = 0
b = 1
while a != 9:
    print("{0}{1}".format(a, b), end="")
    if a != 8 or b != 9:
        print(", ", end="")
    else:
        print("")
    if b == 9:
        a+=1
        b = b -(b - a)
    b+=1
