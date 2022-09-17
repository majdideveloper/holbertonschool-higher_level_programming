#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in range(len(roman_string) - 1):
        if (numbers.get(roman_string[char])
                < numbers.get(roman_string[char + 1])):
            num -= numbers.get(roman_string[char])
        else:
            num += numbers.get(roman_string[char])
    num += numbers.get(roman_string[-1])
    return num
