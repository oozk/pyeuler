#!/usr/bin/env python3
from numba import jit, prange

@jit(nopython=True, parallel=True)
def p145(target):
    result = 0
    for n in prange(1, int(target)):
        if n % 10 != 0:
            if odd_digits(n + reverse(n)):
                result += 1
    return result

@jit(nopython=True)
def reverse(n):
    n_r = 0
    while (n > 0):
        r   = n % 10
        n_r = (n_r * 10) + r
        n   = n // 10
    return n_r

@jit(nopython=True)
def odd_digits(n):
    result = True
    while (n > 0):
        r = n % 10
        if r % 2 == 0:
            result = False
            break
        n = n // 10
    return result

print(p145(1e9))
