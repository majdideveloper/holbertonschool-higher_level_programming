#!/usr/bin/python3
"""function divide matrix """


def matrix_divided(matrix, div):
    """function divide matrix and return matrix of resultat"""
    for row in matrix:
        if not all(isinstance(item, (int, float)) for item in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda item: round(item / div, 2), row))
            for row in matrix]
