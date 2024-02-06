#!/usr/bin/python3
"""
Module 6-load_from_json_file

-Contains  a function that creates an Object from a “JSON file”
-File permissions/exceptions management not included
"""
import json


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        my_obj = json.load(f)
        return my_obj
