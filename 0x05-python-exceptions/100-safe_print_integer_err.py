#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="\n")
        return True
    Exception:
        value_type = value.__class__.__name__
        print("Exception: Unknown format code {} for object of type {}".format(
            value, value_type), file=sys.stderr)
        return False
