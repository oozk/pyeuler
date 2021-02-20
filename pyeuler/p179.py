#!/usr/bin/env python3

from numba import jit
import numpy as np

@jit(nopython=True)
def p179(N):
    divcount = np.full(int(N + 1), 2, dtype=np.int32)
    for i in range(2, int(N + 1) // 2):
        divcount[2 * i :: i] += 1

    result = 0
    for n in range(2, int(N)):
        if divcount[n] == divcount[n+1]:
            result += 1
    return result

print(p179(1e7))
