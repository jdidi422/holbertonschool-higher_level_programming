#!/usr/bin/python3
"""
module documentation
"""


def append_write(filename="", text=""):
    """
    function documentation
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
