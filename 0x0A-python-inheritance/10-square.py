#!/usr/bin/python3
"""
A class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiation with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
