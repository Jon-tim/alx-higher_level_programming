#!/usr/bin/python3
# Write a function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
        new_list = list(map(lambda i: replace if i == search else i, my_list))

    return new_list
