#!/usr/bin/python3
"""
a function that appends a string to a text file (UTF8)
and returns the number of characters written
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of the file to be written
        text: text to be written
        Returns:
            number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return len(text)
