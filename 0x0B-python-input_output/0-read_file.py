#!/usr/bin/python3
"""a function that reads a text file and prints it to the stdout"""


def read_file(filename=""):
    """
    Args:
        filename: name of the file to be read
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read())
