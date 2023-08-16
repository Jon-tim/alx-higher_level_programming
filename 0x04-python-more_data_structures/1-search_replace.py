#!/usr/bin/python3
# Write a function that replaces all occurrences of an element by another in a new list.

def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return my_list

    new_list = []
    
    for i in my_list:
         if i == search:
             i = replace
         new_list.append(i)

    return new_list
