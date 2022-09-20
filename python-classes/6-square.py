#!/usr/bin/python3
"""class square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value[0], int) or  not isinstance(value[1], int) 
        or not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for column in range(self.__size):
            for space in range(int(self.__position[0])):
                print(" ", end="")
            for line in range(self.__size):
                if line == self.__size - 1:
                    print("#")
                    break
                print("#", end="")
