#!/usr/bin/python3
# function that adds all unique integers in a list.
from functools import reduce


def uniq_add(my_list=[]):
    # use set to get unique number
    unique_list = set(my_list)
    summation = 0

    for x in unique_list:
        summation += x
    return summation
