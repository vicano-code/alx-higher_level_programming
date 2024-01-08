#!/usr/bin/python3
# function that removes all characters c and C from a string
def no_c(my_string):
    newStr = ""
    for i in range(0, len(my_string)):
        if my_string[i] not in ['c', 'C']:
            newStr += my_string[i]
    return newStr
