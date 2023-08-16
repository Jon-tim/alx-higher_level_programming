#!/usr/bin/python3
# Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maximum = 0
    holder = ""
    for key, value in a_dictionary.items():
        if a_dictionary[key] > maximum:
            maximum = a_dictionary[key]
            holder = key
        else:
            holder = None
    return holder
