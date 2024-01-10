#!/usr/bin/python3

'''
weighted average of all integers tuple (<score>, <weight>)
'''


def weight_average(my_list=[]):
    if len(my_list) < 1:
        return 0
    mult = 0
    sum_wt = 0
    for x in my_list:
        mult += (x[0] * x[1])
        sum_wt += x[1]
    weighted_avg = mult / sum_wt
    return weighted_avg
