#!/usr/bin/env python3

###
# Problem 69
# https://projecteuler.net/problem=69
###

from tqdm import tqdm
import numba as nb
import numpy as np

n = int(1e12)

def p069():
    return tot(np.zeros(n, np.int32))

@nb.njit("i8(i4[:])", locals=dict(
    n=nb.int32, s=nb.int64, i=nb.int32,
    j=nb.int32, q=nb.int32, f=nb.int32))
def tot(phi):
    s = 0
    maximum = 0
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

        k = i / phi[i]
        if k > maximum:
            maximum = k
            s = i

    return s

print(p069())
