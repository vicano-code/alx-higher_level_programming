#!/usribin/python3
"""
Module 1-write_file

-Contains a function that writes a string to a text file (UTF8)
and returns the number of characters written
-The function creates the file if doesn’t exist and overwrites
the content of the file if it already exists
-file permissions and exceptions not included
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns
    the number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        nwrite = f.write(text)
        return nwrite
