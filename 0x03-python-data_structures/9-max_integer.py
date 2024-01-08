#!/usr/bin/python3

# a function that finds the biggest integer of a list
def max_integer(my_list=[]):
    size = len(my_list)
    biggest_integer = my_list[0]
    if size == 0:
        return None
    for i in range(1, size):
        if my_list[i] > biggest_integer:
            biggest_integer = my_list[i]
    return biggest_integer

