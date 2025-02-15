#!/usr/bin/python3
"""
module documentation
"""
import json


def load_from_json_file(filename):
    """
    function documentation
    """
    with open(filename, "r") as f:
        return json.load(f)
