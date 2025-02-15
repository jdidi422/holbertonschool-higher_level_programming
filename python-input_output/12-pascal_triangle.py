#!/usr/bin/python3
"""
module documentation
"""


def pascal_triangle(n):
    """
    function documentation
    """
    if n <= 0:
        return []

    matrix = []
    for i in range(n):
        row = [1]
        if i > 0:
            prev = matrix[-1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
        matrix.append(row)
    return matrix
