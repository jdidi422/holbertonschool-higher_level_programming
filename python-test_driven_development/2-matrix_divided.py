#!/usr/bin/python3

"""
module documentation
"""


def matrix_divided(matrix, div):
    """
    function documentation
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix of integers/floats")
    if not all(isinstance(elm, (int, float)) for row in matrix for elm in row):
        raise TypeError("matrix must be a matrix of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            divided_row.append(round(element / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix
