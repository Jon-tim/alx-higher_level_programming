#!/usr/bin/python3

# Write a program that prints the ASCII alphabet
# in lowercase, not followed by a new line.


for char in range(ord("a"), ord("z") + 1):
    if char != ord("q") and char != ord("e"):
        print("{:c}".format(char), end='')
