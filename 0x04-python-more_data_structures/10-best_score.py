#!/usr/bin/python3

'''returns a key with the biggest integer value.'''


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = 0
    key_max = ""
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            key_max = key
    return key_max
