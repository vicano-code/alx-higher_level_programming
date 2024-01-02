#!/usr/bin/python3
def pow(a, b):
    ans = 1
    for _ in range(abs(b)):
        if b >= 0:
            ans *= a
        else:
            ans *= 1 / a 
    return ans
