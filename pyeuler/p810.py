#!/usr/bin/env python3

import numpy as np
from numba import njit

@njit
def p810(M, N):

    S = np.full(2**M, True, dtype=np.bool_)
    c = 1

    for i in range(3, 2**M, 2):
        if S[i]:

            c    += 1
            if c == int(N):
                return i

            l = np.ceil(np.log2(i))
            for j in range(l-1, M-l+1):
                k = i<<j
                for l in range(1, 2**j+1):
                    S[k] = False
                    k   ^= i*(l&-l)

    return 0

print(p810(27, 5e6))
