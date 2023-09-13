#!/usr/bin/python3
"""
a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
"""


class Student:
    """
    class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the class
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation
        of a Student instance
        Args:
                attrs: list of attributes
        """
        if attrs is None:
            return self.__dict__

        if type(attrs) is list:
            return {item: self.__dict__[item]
                    for item in attrs if item in self.__dict__.keys()}
