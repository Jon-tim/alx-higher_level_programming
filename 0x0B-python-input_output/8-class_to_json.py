#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object:
"""
to_json_string = __import__('3-to_json_string').to_json_string


def class_to_json(obj):
    """
    Args:
        obj: an instance of a class
    Returns:
        dictionary description with simple data
        structure for JSON serialization
        of an object
    """
    return to_json_string(obj.__dict__)
