#!/usr/bin/python3
"""
Module 0-read_file

Read a text file (UTF8) and print to STDOUT
"""


def read_file(filename=""):
    """read text file and print to stdout """

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
