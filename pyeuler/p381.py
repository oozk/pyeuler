#!/usr/bin/env python3

import numpy as np
from sympy import mod_inverse

def p381(s, e):
    result = 0
    sieve = np.full(int(e), True, dtype=np.bool_)
    for i in range(2, int(e)):
        if sieve[i]:
            sieve[i * i :: i] = False
            if i > 4:
                result += (i - 3) * mod_inverse(8 % i, i) % i

    return result

print(p381(5, 1e8))
