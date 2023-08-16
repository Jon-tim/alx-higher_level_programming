#!/usr/bin/python3
# Write a function that returns a key with the biggest integer value.

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maximum = list(a_dictionary.keys())[0]
    holder = ""
    for key, value in a_dictionary.items():
        if value > maximum:
            maximum = value
            holder = key
    return holder
