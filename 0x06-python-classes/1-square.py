#!/usr/bin/python3

"""
Write a class Square that defines a square by: (based on 0-square.py)

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module

"""


class Square:
    """A class that creates and defines a square"""

    def __init__(self, size):
        """
        Args:
            size: the provided size of the square.
        """
        self.__size = size
