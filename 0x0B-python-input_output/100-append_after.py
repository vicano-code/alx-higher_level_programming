#!/usr/bin/python3
"""
Module 100-append_after.py

-Contains a function that inserts a line of text to a file, after
each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after
    each line containing a specific string
    """
    with open(filename, mode='r+', encoding="utf-8") as f:
        txt = ""
        for line in f:
            txt += line
            if line.find(search_string) != -1:
                txt += new_string

        f.seek(0)
        f.write(txt)
