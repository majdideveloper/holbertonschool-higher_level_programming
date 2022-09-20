#!/usr/bin/python3
"""class square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for column in range(self.__size):
            for line in range(self.__size):
                if line == self.__size - 1:
                    print("#")
                    break
                print("#", end="")
