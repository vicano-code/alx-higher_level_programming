#!/usr/bin/python3

# a function that finds the biggest integer of a list
def max_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        return None
    biggest_integer = my_list[0]
    for i in range(1, size):
        if my_list[i] > biggest_integer:
            biggest_integer = my_list[i]
    return biggest_integer
