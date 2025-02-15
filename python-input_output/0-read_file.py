#!/usr/bin/python3
"""
module documentation
"""


def read_file(filename=""):
    """
    function documentation
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
