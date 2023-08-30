#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 4-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            size must be an integer, otherwise
            raise a TypeError exception with the message:
            size must be an integer
            if size is less than 0,
            raise a ValueError exception with the message:
            size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
    that prints in stdout the square with the character #:
        if size is equal to 0, print an empty line
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

    def area(self):
        """function that calculates the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """function that prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """property function that retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        property function that sets the size
        Args:
            value: the given value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
