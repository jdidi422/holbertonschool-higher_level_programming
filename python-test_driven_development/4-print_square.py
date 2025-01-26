#!/usr/bin/python3
"""
This module provides a function that prints a squar of #

Examples:
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Walter", "White")
My name is Walter White
>>> say_my_name("Bob")
My name is Bob
>>> say_my_name(12, "White")
Traceback (most recent call last):
    ...
TypeError: first_name must be a string
>>> say_my_name("John", 123)
Traceback (most recent call last):
    ...
TypeError: last_name must be a string
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
    size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer
    or if size is a float and is less than 0.
    ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
