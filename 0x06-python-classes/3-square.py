#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
        size must be an integer, otherwise raise a-
        TypeError exception with the message:
        size must be an integer
        if size is less than 0, raise a-
        ValueError exception with the message:
        size must be >= 0
    You are not allowed to import any module
"""


class Square:
    """A class that defines and creates a square"""

    def __init__(self, size=0):
        """
        Args:
            size: an integer given size
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """A function that calculates the area of a square"""
        return self.__size * self.__size
