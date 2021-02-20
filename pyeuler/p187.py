#!/usr/bin/env python3

import numpy as np
from numba import jit

@jit
def p187(N):
    sieve    = np.full(int(N + 1), True, dtype=np.bool_)
    sieve[0] = sieve[1] = False
    for i in range(2, int(N**.5) + 1):
        if sieve[i]: sieve[i * i :: i] = False
    primes, sieve = [i for i, b in enumerate(sieve) if b], []

    result   = 0
    for i in range(0, len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] < N:
                result += 1
            else:
                break
    return result

print(p187(1e8))
