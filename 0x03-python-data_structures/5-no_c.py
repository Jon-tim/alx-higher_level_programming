#!/usr/bin/python3
def no_c(my_string):
    array = [i for i in my_string if i != 'c' and i != 'C']
    new_string = "".join(array)

    return new_string
