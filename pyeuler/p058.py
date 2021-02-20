#!/usr/bin/env python3

###
# Problem 78
# https://projecteuler.net/problem=78
###

from sympy import isprime

def p058(l):

    getidx = lambda x, i: [x + 2 * i * j for j in range(1, 5)]
    i, idx = 0, [1]
    numerator, denominator, r = 0, 1, 1
    while r > l:
        i += 1
        idx = getidx(idx[-1], i)
        numerator   += sum(1 for i in idx if isprime(i))
        denominator += 4
        r = numerator / denominator

    return 2 * i + 1, '{:.5%}'.format(r)


print(p058(0.1))
