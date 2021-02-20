#!/usr/bin/env python3

from numba import jit
import numpy as np

@jit(nopython=True)
def p278(N):

    sieve      = np.full(N+1, True, dtype=np.bool_)
    for i in range(2, int(N**.5) + 1):
        if sieve[i]: sieve[2 * i :: i] = False
    primes     = [i for i, b in enumerate(sieve) if b and i > 1]

    result     = 0
    for p in primes:
        for q in primes:
            if p < q:
                for r in primes:
                    if q < r:
                        result += 2 * (p * q * r) - (p*q + p*r + q*r)
    return result

print(p278(5000))
