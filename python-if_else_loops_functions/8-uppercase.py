#!/usr/bin/python3
def uppercase(str):
    lenStr = len(str)
    newStr = ""
    for char in range(lenStr):
        c = ord(str[char])
        if c >= 97 and c <= 122:
            newStr = newStr + chr(c - 32)
        else:
            newStr = newStr + str[char]
    print(newStr)
