#!/usr/bin/env python3

###
# Problem 70
# https://projecteuler.net/problem=70
###

import numba as nb
import numpy as np

n = int(1e7)

def p070():
    phi = np.zeros(n, np.int32)
    result = tot(phi)
    return result

@nb.njit(Parallel=False)
def check_perm(i, phi):
    perm = lambda x, y : ''.join(sorted([a for a in str(x) + ' '])).strip() == ''.join(sorted([a for a in str(y) + ' '])).strip()
    if perm(i, phi):
        return i / phi
    else:
        return 99999999999

@nb.njit("i8(i4[:])", locals=dict(
    n=nb.int32, s=nb.int64, i=nb.int32,
    j=nb.int32, q=nb.int32, f=nb.int32))
def tot(phi):
    s = 0
    minimum = 99999999999
    r = 0
    phi[1] = 1
    i = 1
    while i <= n:
        i += 1
        if phi[i] == 0:
            phi[i] = i - 1
            j = 2
            while j * i < n:
                if phi[j] != 0:
                    q = j
                    f = i - 1
                    while q % i == 0:
                        f *= i
                        q //= i
                    phi[i * j] = f * phi[q]
                j += 1
        r = check_perm(i, phi[i])
        if minimum < r:
            minimum = r
            s = i
    return s

print(p070())
