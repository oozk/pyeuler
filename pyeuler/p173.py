#!/usr/bin/env python3

from sympy import divisors

def p173(N):
    return sum(1 for n in range(1, int(N/4)+1) for x in divisors(n) if x < n**.5)

print(p173(1e6))
