#!/usr/bin/python3
def remove_char_at(str, n):
    lenStr = len(str)
    newStr = ""
    for indexChar in range(lenStr):
        if n != indexChar:
            newStr = newStr + str[indexChar]
    return newStr
