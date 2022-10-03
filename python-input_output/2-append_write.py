#!/usr/bin/python3
"""This module  contains function that appends a string at the end of a text
file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Parameters
    ----------
    filename : str
        The file name written in
    text : str
        text to write in the file

    Returns
    -------
    int
        the number of characters added
   """
    with open(filename, 'a', encoding="utf-8") as f:
        numberCara = f.write(text)
    f.close()
    return numberCara
