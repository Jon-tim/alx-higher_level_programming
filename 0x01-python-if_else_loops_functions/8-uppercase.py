#!/usr/bin/python3

# Write a function that prints a string in uppercase followed by a new line.

def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("{}".format(" "))