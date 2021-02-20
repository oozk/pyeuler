#!/usr/bin/env python3

from numba import jit, prange
import numpy as np
from math import gcd

@jit(nopython=True, parallel=True)
def p329(N, C):

    sieve      = np.full(N+1, True, dtype=np.bool_)
    sieve[0]   = sieve[1] = False
    for i in range(2, int(N**.5) + 1):
        if sieve[i]: sieve[2 * i :: i] = False

    def isprime(n):
        if sieve[n]: return 'P'
        return 'N'

    def jumps(n, M):
        res    = np.full(M, 1, dtype=np.int64)
        c      = 1
        while n >= 1:
            if n%2 != 0: res[-c] = -1
            n //= 2
            c  += 1
        return res

    M          = len(C)-1
    p, q       = 0, N * 2 ** M * 3 ** (M+1)
    for i in prange(1, N+1):
        for j in range(0, 2**M):
            sq, num = i, 1
            if isprime(sq) == C[0]: num *= 2
            for k, l in np.ndenumerate(jumps(j, M)):
                if sq  <= 1:
                    sq  = 2
                elif sq  >= N:
                    sq  = N-1
                else:
                    sq += l
                if isprime(sq) == C[k[0]+1]: num *= 2
            p += num

    return (p // gcd(p, q), q // gcd(p, q))

print('%s/%s' % p329(500, 'PPPPNNPPPNPPNPN'))
