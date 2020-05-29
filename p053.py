#!/usr/bin/env python3

###
# Problem 53
# https://projecteuler.net/problem=53
###

from math import factorial

def p053(l):
    factorials = dict((i, factorial(i)) for i in range(0, l+1))
    n_choose_r = lambda n, r: factorials[n] / factorials[r] / factorials[n-r]
    return sum(1 for n in range(1, l+1) for r in range(1, n) if n_choose_r(n, r) > 1e6)

print(p053(100))
