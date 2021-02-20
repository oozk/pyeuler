#!/usr/bin/env python3

###
# Problem 69
# https://projecteuler.net/problem=69
###

import numba as nb
import numpy as np

@nb.jit
def p069(n):

    dt = np.dtype(np.float32)
    totients = np.array([x for x in np.arange(n + 1, dtype=dt)])

    for i in range(2, len(totients)):
        if totients[i] == i:
            for j in range(i, len(totients), i):
                totients[j] -= totients[j] // i
        totients[i] = i / totients[i]

    return np.argmax(totients)

print(p069(1e6))
