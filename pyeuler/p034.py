#!/usr/bin/env python3

###
# Problem 34
# https://projecteuler.net/problem=34
###

from math import factorial

def p034():
    digitfact = dict((str(i), factorial(i)) for i in range(0, 10))
    digitsum = lambda n: n == sum(digitfact[s] for s in str(n))
    return sum(n for n in range(3, 7 * factorial(9)) if digitsum(n))

print(p034())
