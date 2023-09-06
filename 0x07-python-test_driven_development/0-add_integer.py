#!/usr/bin/python3
"""
function that adds two integers
a and b must be integers or floats
a and b must be first cast to integers if they are float
"""


def add_integer(a, b=98):
    """
    Returns the result of the addition of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
