#!/usr/bin/env python3

import numpy as np
from numba import jit

@jit
def p204(k, N):

    sieve   = np.full(int(N + 1), True, dtype=np.bool_)
    hamming = np.full(int(N + 1), False, dtype=np.bool_)

    sieve[0] = sieve[1] = False
    hamming[1] = True

    for i in range(2, int(N // 2) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
            if i <= k:
                hamming[i :: i] = True
            else:
                hamming[i :: i] = False

    return np.count_nonzero(hamming)

print(p204(100, 1e9))

    # sieve      = bytearray(b'\x01'*int(N+1))
    # sieve[:1]  = b'\x00\x00'
    # hamming    = bytearray(b'\x00'*int(N+1))
    # hamming[1] = 1
    # for i in range(2, int(N // 2) + 1):
    #     if sieve[i]:
    #         sieve[2*i :: i] = bytearray(int(N-2*i+1)//i + 1)
    #         if i <= k:
    #             hamming[i] = 1
    #             hamming[2*i :: i] = bytearray(b'\x01' * (int(N-2*i)//i + 1))
    #         else:
    #             hamming[2*i :: i] = bytearray(int(N-2*i)//i + 1)
