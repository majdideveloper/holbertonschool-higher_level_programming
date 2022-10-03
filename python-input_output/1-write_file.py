#!/usr/bin/python3
"""This module  contains function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Parameters
    ----------
    filename : str
        The file name written in
    text : str
        text to write in the file

    Returns
    -------
    int
        the number of characters written
   """
   with open(filename, 'r', encoding="utf-8") as f:
       numberCara = f.write(text)
       print(numberCara)
   f.close()
