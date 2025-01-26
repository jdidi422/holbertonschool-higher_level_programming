#!/usr/bin/python3
"""
This module provides a function to devide amatrix

Examples:
>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
>>> matrix_divided([[10, 20], [30, 40]], 10)
[[1.0, 2.0], [3.0, 4.0]]
>>> matrix_divided([[1, -2, 3], [-4, 5, -6]], -2)
[[-0.5, 1.0, -1.5], [2.0, -2.5, 3.0]]
>>> matrix_divided([[5, 10], [15, 20]], 0.5)
[[10.0, 20.0], [30.0, 40.0]]
>>> matrix_divided([[1, 2], [3, 4]], 0)
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
>>> matrix_divided([[1, 2, 3], [4, 5, 6]])
Traceback (most recent call last):
    ...
TypeError: missing 1 required positional argument: 'div'
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    (div), rounding the result to 2 decimal places.

    Args:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The number by which
    each element of the matrix will be divided.

    Returns:
    list of lists of float: A new matrix with each element divided by div and
    rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats.
    TypeError: If rows of the matrix do not have the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is 0.
    """

    if div is None:
        raise TypeError("missing 1 required positional argument: 'div'")

    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not all(isinstance(item, (int, float))
               for row in matrix for item in row):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    row_size = len(matrix[0])

    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
