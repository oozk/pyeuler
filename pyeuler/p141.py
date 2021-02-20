#!/usr/bin/env python3

from numba import njit

@njit(nopython=True)
def p141(l):
    is_int  = lambda x: x - int(x) == 0
    result  = 0
    for d in range(2, int(l ** (1/2))):
        d2 = (d ** 2)
        for r in range(1, q):
            if d2 % r == 0:
                n = (d2 * d // r + r)
                if n < l and is_int(n ** .5):
                    result += int(n)
                    print(r, d, n, result)
                    # print(factorint(r))

    return result

print(p141(1e12))
