#!/usr/bin/python3
"""
This module provides a function to add two integers.

Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, rounding them to the nearest integer.

    Args:
    a (int, float): The first integer or float.
    b (int, float): The second integer or float. Default is 98.

    Returns:
    int: The sum of a and b after rounding them.

    Raises:
    TypeError: If a or b is not an integer or float.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return round(a) + round(b)
