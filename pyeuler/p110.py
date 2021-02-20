#!/usr/bin/env python3

from math import log, floor
from sympy import prime
from functools import reduce
from operator import mul

def toBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits += [int(n % b)]
        n //= b
    return digits

def convertExp(nb, exp, primes, n):
    powers = []
    if len(nb) < len(exp):
        nb += [0] * (len(exp) - len(nb))
    for i, x in enumerate(nb[::-1]):
        while x > 0:
            powers += [(exp[::-1][i] - 1) // 2]
            x -= 1
    return reduce(mul, [primes[i] ** j for i, j in enumerate(powers)],1)

def p108(LIMIT):
    m          = floor(log(2 * LIMIT) / log(3)) + 1
    depth      = m // 2 + 1
    primes     = [prime(i) for i in range(1, m+1)]
    divfactor  = [2*i + 1 for i in range(1, depth)]
    divcount   = lambda i: reduce(mul, [divfactor[j] ** k for j, k in enumerate(toBase(i, m))], 1)
    makenum    = lambda i: convertExp(toBase(i, m), divfactor, primes, m)

    t1, t2, t3 = 0, 0, 0
    best       = 2 * LIMIT
    result     = reduce(mul, primes, 1)
    for i in range(1, m ** (depth-1)):
        t1 = divcount(i) - 2 * LIMIT
        if 0 < t1 <= best:
            t2  = makenum(i)
            t3 += 1
            if t2 < result:
                t3     = 0
                best   = t1
                result = t2
                print('Best so far:', result)
            else:
                if t3 >= depth:
                    break

    return result

print('Solution:', p108(112))
print('Solution:', p108(1e3))
print('Solution:', p108(4e6))
