#!/usr/bin/python3
"""
Module 5-text_indentation

-function that prints a text with 2 new lines after each
of these characters: ., ? and :
-text must be a string
-no space at the beginning or at the end of each printed line
"""


def text_indentation(text):
    """
    prints a text based on the module description
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    i = 0
    size = len(text)
    while i < size:
        print("{}".format(text[i]), end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            while (i + 1) < size and text[i + 1] == " ":
                i += 1
                continue
        i += 1
