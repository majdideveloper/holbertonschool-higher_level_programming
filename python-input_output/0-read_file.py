#!/usr/bin/python3
"""this module contains function that read file and print as output"""


def read_file(filename=""):
    """Funtion that read file and print as output

    Parameters
    ----------
    filename : str
        The file name to read and ptint
    """
    with open(filename, 'r', encoding="utf-8") as f:
        fileRead = f.read()
        print(fileRead, end="")
    f.close()
