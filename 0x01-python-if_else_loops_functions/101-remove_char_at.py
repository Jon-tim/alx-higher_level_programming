#!/usr/bin/python3


def remove_char_at(str, n):
    new = ""
    for c in range(len(str)):
        if c != n:
            new += str[c]
    return new
