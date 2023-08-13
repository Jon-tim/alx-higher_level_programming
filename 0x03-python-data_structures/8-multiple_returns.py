#!/usr/bin/python3
def multiple_returns(sentence):
    first = sentence[0]
    length = len(sentence)
    if sentence == None:
        first = None
    return (length, first)
