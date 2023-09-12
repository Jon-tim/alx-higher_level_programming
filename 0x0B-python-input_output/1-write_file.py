#!/usr/bin/python3
"""
a function that writes a string to a text file (UTF8)
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Args:
        filename: name of the file to be written
        text: text to be written
    Returns:
        number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return len(text)
