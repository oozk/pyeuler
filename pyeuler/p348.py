#!/usr/bin/env python3

from math import log10
from numba import jit
from numba.types import int64
from numpy import empty, append, sum

@jit(nopython=True)
def p348(N, L):

    def revnum(n):
        result = 0
        while(n):
            r = n % 10
            result = result * 10 + r
            n //= 10
        return result

    def check_property(p):
        count = 0
        for y in range(1, int(p ** (1/3)) + 1):
            x = (p - y**3)**.5
            if x - int(x) == 0: count += 1
        if count == 4:
            return True
        return False

    def make_odd_palindromes(N):
        p = empty(0, dtype=int64)
        for n in range(1,  10 ** int(N)):
            r = revnum(n)
            if r % 2 != 0:
                x = n * 10**int(log10(n)+1) + r
                if check_property(x): p = append(p, x)
                x = n//10 * 10**int(log10(n)+1) + r
                if check_property(x): p = append(p, x)
        return p

    return sum(make_odd_palindromes(N)[:L])

print(p348(5, 5))
