#!/usr/bin/env python3
###
# Problem 43
# https://projecteuler.net/problem=43
# Sub-string divisibility
###
import cProfile
from itertools import permutations

def p043():
    pandigits = range(0, 10)
    primes = [2, 3, 5, 7, 11, 13, 17]
    divisible = lambda n: all((100*n[i+1]+10*n[i+2]+n[i+3]) % p == 0 for i, p in enumerate(primes))
    list2num = lambda l: sum(10 ** (len(l)-i-1) * v for i, v in enumerate(l))
    return sum(list2num(p) for p in permutations(pandigits) if divisible(p))

cProfile.run('print(p043())')
