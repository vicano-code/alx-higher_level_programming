#!/usr/bin/python3

# function that adds 2 tuples.
def add_tuple(tuple_a=(), tuple_b=()):
    size_a = len(tuple_a)
    size_b = len(tuple_b)
    if size_a == 0 and size_b == 0:
        return ()
    if size_a == 0:
        return tuple_b
    if size_b == 0:
        return tuple_a
# tuples are immutable so convert to list
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) < 2:
        list_a.append(0)
    if len(list_b) < 2:
        list_b.append(0)
# obtain the result and convert back to tuple
    result = tuple((map(lambda x, y: x + y, list_a[:2], list_b[:2])))

    return result
