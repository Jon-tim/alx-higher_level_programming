#!/usr/bin/python3
"""
Write a function that returns True if the object is an
instance of a class that inherited (directly or
indirectly) from the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """
    Args:
    obj: object
        a_class: class
    Returns:
        True if obj is an instance of a class that
        inherited (directly or indirectly) from a_class;
        otherwise False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
