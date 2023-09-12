#!/usr/bin/python3
"""
A class BaseGeometry
"""


class BaseGeometry:
    """
    A class BaseGeometry
    """

    def area(self):
        """
        raises an Exception with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates a value
        Args:
            name: name of the value
            value: value to be validated
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
