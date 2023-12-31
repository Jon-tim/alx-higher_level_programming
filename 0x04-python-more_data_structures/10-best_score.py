#!/usr/bin/python3
# Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    maximum = 0
    holder = ""
    for key, value in a_dictionary.items():
        if value > maximum:
            maximum = value
            holder = key
    return holder
