#!/usr/bin/python3
def islower(c):
    c = ord(c)
    if c >= 33 and c <= 57 or c >= 65 and c <= 90:
        return False
    else:
        return True
