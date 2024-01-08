#!/usr/bin/python3

'''
function that deletes the item at a specific position in a list.
'''


def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if idx < 0 or idx >= size:
        return my_list
    del my_list[idx]
    return my_list
