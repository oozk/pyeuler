#!/usr/bin/env python3

from math import gcd
from numba import jit, prange

@jit(nopython=True, parallel=True)
def p127(l):
    rad    = [0] + [1] * l
    for i in range(1, l):
        if rad[i] == 1:
            for j in range(i, l, i): rad[j] *= i

    result = 0
    for a in prange(1, l // 2 + 1):
        for b in range(a + 1, l - a + 1):
            c = a + b
            if rad[a] * rad[b] > c: continue
            if c < l and rad[a] * rad[b] * rad[c] < c and gcd(a, b) == 1:
                result += c

    return result

print(p127(120000))
