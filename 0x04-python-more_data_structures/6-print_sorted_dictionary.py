#!/usr/bin/python3

''' prints a dictionary by ordered keys'''


def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())
    for key in sorted_dict:
        print(f"{key}: {a_dictionary[key]}")
