#!/usr/bin/python3
"""
a function that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: object to be converted to JSON
    Returns:
        JSON representation of my_obj
    """
    return json.dumps(my_obj)
