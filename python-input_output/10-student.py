#!/usr/bin/python3
"""
module documentation
"""


class Student:
    """
    function documentation
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
