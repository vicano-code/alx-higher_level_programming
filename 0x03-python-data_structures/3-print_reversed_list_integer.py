#!/usr/bin/python3

# function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    size = len(my_list)
    if size == 0:
        print("".format())
    my_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
