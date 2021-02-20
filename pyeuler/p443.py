#!/usr/bin/env python3

from math import gcd
from sympy import isprime

def p443(N):
    n, g  = 4, 13
    while n < N:
        p = 2 * n - 1
        if g == 3 * n and isprime(p):
            if p <= N:
                n, g = p, 3 * p
                print(n)
            else:
                n, g = N, g + (N - n)
        else:
            n += 1
            g += gcd(n, g)

    return int(g)

print(p443(1e15))
