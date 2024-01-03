#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = str[:]
    if n < 0:
        return str_copy
    else:
        return str_copy[0:n] + str_copy[n+1:]
