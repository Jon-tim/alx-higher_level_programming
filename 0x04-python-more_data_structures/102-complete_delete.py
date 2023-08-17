#!/usr/bin/python3
# Write a function that deletes keys with a
# specific value in a dictionary.

def complex_delete(a_dictionary, value):

    store = []
    for key, val in a_dictionary.items():
        if val == value:
            store.append(key)
    for item in store:
        del a_dictionary[item]
    return a_dictionary
