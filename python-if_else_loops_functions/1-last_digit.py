#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    number = -1 * number
    sign = -1
num = (number % 10) * sign
if num > 5:
    print(f"Last digit of {number * sign} is {num} and is greater than 5")
if num == 0:
    print(f"Last digit of {number * sign} is {num} and is 0")
if num < 6 and num != 0:
    print(f"Last digit of {number * sign}
            is {num} and is less than 6 and not 0")
