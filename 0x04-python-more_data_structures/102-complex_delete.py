#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    del_list = []
    for key, val in a_dictionary.items():
        if val == value:
            del_list.append(key)
    for i in del_list:
        a_dictionary.pop(i, None)
    return a_dictionary
