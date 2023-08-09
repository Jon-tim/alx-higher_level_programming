#!/usr/bin/python3

i = ord('z')

while i > ord('a') - 1:
    print("{}".format(chr(i - 32) if i % 2 != 0 else chr(i)), end="")
    i -= 1
