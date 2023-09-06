#!/usr/bin/python3
"""
function that prints a fullname
first_name and last_name must be strings
otherwise raise a TypeError exception
"""


def say_my_name(first_name, last_name=""):
    """
    Returns fullname
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")

    if last_name:
        full_name = "{} {}".format(first_name, last_name)
    else:
        full_name = first_name

    print("My name is {}".format(full_name))
