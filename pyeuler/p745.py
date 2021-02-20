#!/usr/bin/env python3

from numba import jit
import numpy as np

@jit(nopython=True)
def p745(N):

    result = 0
    sieve  = np.full(int(N**.5)+1, 1, dtype=np.int64)
    for i in range(len(sieve), 0, -1):
        sieve[i] = N//(i**2) - np.sum(sieve[2*i :: i])
        result  += sieve[i] * (i**2) % (1e9+7)
    return int(result % (1e9+7))

print(p745(1e14))
