#!/usr/bin/python3
# Write a function that returns
# the weighted average of all integers tuple (<score>, <weight>)

def weight_average(my_list=[]):
    if not my_list:
        return 0

    new = list(map(lambda item: item[0] * item[1], my_list))
    average = sum(y for _, y in my_list)
    summation = 0

    for number in new:
        summation += number

    weighted_average = summation / average

    return weighted_average
