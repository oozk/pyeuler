#!/usr/bin/env python3

from numba import njit
import numpy as np

def p070(lim):

    permi = lambda n, f: sorted(str(n)) == sorted(str(f))
    tots  = totient_sieve(int(lim))
    print(tots)
    pool  = [(i, t) for i, t in enumerate(tots[2:], 2) if permi(i, t)]
    return min(pool, key=lambda n: n[0] / n[1])[0]

# @njit #(nopython=True)
def totient_sieve(n):
    totients = np.array(range(n + 1))
    print(totients)
    for i in range(2, len(totients)):
        if totients[i] == i:
            for j in range(i, len(totients), i):
                totients[j] -= totients[j] // i
    return totients

print(p070(1e6))
