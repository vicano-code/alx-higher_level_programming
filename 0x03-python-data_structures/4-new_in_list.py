#!/usr/bin/python3

'''
function that replaces an element in a list at a specific
position without modifying the original list
'''


def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        my_list_copy = my_list.copy()
        my_list_copy[idx] = element
        return my_list_copy
    return my_list
