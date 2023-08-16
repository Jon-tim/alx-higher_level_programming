#!/usr/bin/python3
# Write a function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    # to solve this using MAP, LAMBDA and LIST:
    newMatrix = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    # to solve this using LIST COMPREHENSION:
    # newMatrix = [[y * y for y in x] for x in matrix]
    return newMatrix
