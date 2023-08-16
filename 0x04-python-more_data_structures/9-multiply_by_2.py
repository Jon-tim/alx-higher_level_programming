#!/usr/bin/python3
# Write a function that returns a new dictionary
# with all values multiplied by 2


def multiply_by_2(a_dictionary):
    new = {y: y * 2 for x, y in a_dictionary.items()}
    return new
