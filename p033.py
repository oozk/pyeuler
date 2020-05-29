#!/usr/bin/env python3

from math import gcd

def p033():

    dcf  = lambda a, b, c: float(a+b) / float(b+c) == float(a) / float(c) and a != b != c
    res  = lambda a, b, c: (int(a+b) // gcd(int(a+b), int(b+c)), \
                            int(b+c) // gcd(int(a+b), int(b+c)))

    rng  = [str(i) for i in range(1, 10)]
    fractions = (res(a, b, c) for a in rng for b in rng for c in rng if dcf(a, b, c))

    a, b = 1, 1
    for (i, j) in fractions: a, b = a * i, b * j

    return b // gcd(a, b)

print(p033())
