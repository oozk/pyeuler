#!/usr/bin/env python3

from sympy import mod_inverse
from math import log, floor

def p134(N):
    sieve  = [True] * (int(N) + 100)

    p2, result = 2, 0
    for i in range(3, len(sieve), 2):
        if sieve[i]:
            for j in range(2*i, len(sieve), i):
                sieve[j] = False

            p1, p2 = p2, i
            if p2 >= 7:
                m = 10 ** (floor(log(p1) / log(10)) + 1)
                result += ((mod_inverse(p2, m) * p1) % m) * p2
            if p2 > N:
                break

    return result

print(p134(1e6))
