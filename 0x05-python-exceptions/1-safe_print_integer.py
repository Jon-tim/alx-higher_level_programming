#!/usr/bin/python3

def safe_print_integer(value):
    if value:
        try:
            n = int(value)
            print("{:d}".format(n))
        except ValueError:
            return False
    return True
