#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first = 0
    second = 0
    new_tuple = ()

    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a = (tuple_a[0], 0)
        else:
            tuple_a = (0, 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b = (tuple_b[0], 0)
        else:
            tuple_b = (0, 0)

    first = tuple_a[0] + tuple_b[0]
    second = tuple_a[1] + tuple_b[1]
    new_tuple = (first, second)

    return new_tuple
