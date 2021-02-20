#!/usr/bin/env python3

###
# Problem 26
# https://projecteuler.net/problem=26
###

import itertools

def p026():
    return max(range(1, 1000), key=float_repeat_len)

def float_repeat_len(d):
    n = 1 % d
    remainders = []
    while True:
        if n in remainders:
            return len(remainders) - remainders.index(n)
        remainders.append(n)
        n = n * 10 % d

print(p026())
