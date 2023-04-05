#!/usr/bin/env python3

from numpy import log, full, bool_, sum
from numba import jit

@jit(nopython=True)
def p800(N, E):
    L     = E * log(N) / log(2)
    sieve = full(int(L) + 1, True, dtype=bool_)
    sieve[0:2] = False
    for i in range(3, int(L**.5)+1, 2):
        if sieve[i]:
            sieve[i*i :: i] = False

    r = 0
    for p, b in enumerate(sieve):
        if b:
            print(p)
            c  = int(E * log(N-p) / log(p))
            r += sum(sieve[:c])

    return r

print(p800(800, 800))
