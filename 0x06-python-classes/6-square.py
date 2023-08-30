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
    Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
            position must be a tuple of 2 positive integers,
            otherwise raise a TypeError exception with the message
            position must be a tuple of 2 positive integers

    Instantiation with optional size and optional
        position: def __init__(self, size=0, position=(0, 0)):
    Public instance method: def area(self):
    that returns the current square area
    Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
            if size is equal to 0, print an empty line
            position should be used by using space
                - Don’t fill lines by spaces when position[1] > 0
    You are not allowed to import any module
"""


class Square:
    """A class that defines and creates a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: an integer given size
            position: a tuple given position
        """
        self.__size = size
        self.__position = position

    def area(self):
        """function that calculates the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """function that prints in stdout the square with character #"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__size + self.__position[1]):
                if a >= self.__position[1]:
                    for j in range(self.__position[0]):
                        print(" ", end="")
                    for k in range(self.__size):
                        print("#", end="")
                    print()

    @property
    def size(self):
        """property function that retrieves the size"""
        return self.__size

    @property
    def position(self):
        """property function that retrieves the position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """
        Args:
            value: the given value as a tuple
        """
        for item in value:
            if not isinstance(item, int) and item < 0 and len(value) != 2:
                message = "position must be a tuple of 2 positive integers"
                raise TypeError(message)
        self.__position = value
