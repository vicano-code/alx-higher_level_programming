#!/usr/bin/python3

# returns a set of common elements in two sets


def common_elements(set_1, set_2):
    return {x for x in set_1 if x in set_2}

# OR
# return set_1.intersection(set_2)
