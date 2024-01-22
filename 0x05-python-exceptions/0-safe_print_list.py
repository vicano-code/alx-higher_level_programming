#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num_printed = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            num_printed += 1
    except IndexError:
        pass
    print("")
    return num_printed
