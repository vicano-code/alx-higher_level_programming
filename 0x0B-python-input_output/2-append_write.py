#!/usr/bin/python3
"""
Module 2-append_write

-Contains a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added
-file permissions and exceptions not included
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file and
    returns the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
