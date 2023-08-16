#!/usr/bin/python3
# function that adds all unique integers in a list.
from functools import reduce


def uniq_add(my_list=[]):
    # use set to get unique number
    unique_list = set(my_list)
    # use reduce to get the summation
    return reduce(lambda a, b: a + b, unique_list)
