#!/usr/bin/python3
"""
Write a function that returns True if the object is
exactly an instance of the specified class
otherwise False
"""


def is_same_class(obj, a_class):
    """
    Args:
            obj: object
            a_class: class type

    Returns:
            True if the object is exactly an instance
            of the specified class
            Otherwise False
    """
    if obj is not None and a_class is not None:
        if type(obj) is a_class:
            return True
        else:
            return False
