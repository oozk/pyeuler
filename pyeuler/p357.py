#!/usr/bin/env python3

import numpy as np
from sympy import divisors

def p357(l):
    l = int(l)
    sieve = np.full(l+1, True, dtype=bool)
    sieve[0] = sieve[1] = False
    for i in range(2, int(l ** .5) + 1):
        if sieve[i]: sieve[i * i :: i] = False

    result = 2
    for i in range(2, l+1):
        if sieve[i] and not sieve[i-1] and sieve[2 + (i-1)//2]:
            n = i-1
            if all(sieve[d + n//d] for d in divisors(n)):
                result += n

    return result

print(p357(1e8))
