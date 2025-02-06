#!/usr/bin/python3
"""
module documentation
"""


def inherits_from(obj, a_class):
    """
    function documentation
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
