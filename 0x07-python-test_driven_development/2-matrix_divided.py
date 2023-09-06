#!/usr/bin/python3
"""
A function that divides all elements of a matrix.
Matrix must be a list of lists of integers or floats
Matrix rows must be of same size
"""


def matrix_divided(matrix, div):
    """
    Return a new matrix with elements of the matrix
    divided by div, rounded to 2 decimal places
    Args:
        matrix: matrix
        div: integer for division
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if len(matrix) == 0 or len(matrix) < 2:
        raise TypeError(msg)
    for m_list in matrix:
        if not m_list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for item in m_list:
            if type(item) is not int and type(item) is not float:
                raise TypeError(msg)
        if len(matrix[0]) != len(m_list):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(items / div, 2) for items in row] for row in matrix]
