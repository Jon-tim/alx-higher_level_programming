#!/usr/bin/python3
"""
Write a function that returns True if the object is
an instance of, or if the object is an instance of a
class that inherited from, the specified class
otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Args:
            obj: object
            a_class: class type

    Returns:
            True if the object is an instance
            of the specified class
            Otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
