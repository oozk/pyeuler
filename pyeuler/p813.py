#!/usr/bin/env python3

from math import log, floor
from itertools import product

def p813(n, M):

    L = []
    while n > 0:
        p  = pow(2, floor(log(n, 2)))
        L += [(3*p, p, 0)]
        n -= p

    S = set()
    for k in product(range(3), repeat=len(L)):
        S ^= {sum(L[i][j] for i, j in enumerate(k))}

    return sum(pow(2, p, M) for p in S) % M

print(p813(pow(8, 12) * pow(12, 8), int(1e9+7)))  
# print(p813(pow(3, 8), int(1e9+7)))

def p813_2(M):

    def xor(n):
        r = 11
        for i in range(1, n):
            r = r ^ (r << 1) ^ (r << 3)
        return r

    n = xor(pow(3, 8))

    return n

# print(p813_2(int(1e9+7)))
