#!/usr/bin/python3
"""
Module 4-from_json_string

-Contains a function that returns an object (Python data structure)
represented by a JSON string
-Exceptions mgt not included
"""
import json


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
