#!/usr/bin/env python3

from numba import jit
import numpy as np

@jit(nopython=True)
def p193(N):

    sieve  = np.full(int(N**.5)+1, 1, dtype=np.int64)
    for i in range(len(sieve), 0, -1):
        sieve[i] = N//(i**2) - np.sum(sieve[2*i :: i])
    return sieve[1]

print(p193(2**50))
