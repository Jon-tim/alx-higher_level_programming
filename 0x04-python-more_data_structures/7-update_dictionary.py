#!/usr/bin/python3
# Write a function that replaces or adds key/value in a dictionary.

def update_dictionary(a_dictionary, key, value):

    if key in list(a_dictionary):
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
