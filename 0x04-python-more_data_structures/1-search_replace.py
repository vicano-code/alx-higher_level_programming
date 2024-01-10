#!/usr/bin/python3

'''replaces all occurrences of an element by another in a new list'''


def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in new_list:
        if i == search:
            idx = new_list.index(i)
            new_list[idx] = replace
    return new_list
