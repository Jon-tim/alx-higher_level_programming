#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Args:
            width: width of a rectangle
            height: height of a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property that retrieves the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        property that sets the rectangle's width
        Args:
            value: the given value
        Returns:
            the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property that sets the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        property that sets the rectangle's height
        Args:
            value: the given value
        Returns:
            the height
        Raises:
            TypeError: if value isn't integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
