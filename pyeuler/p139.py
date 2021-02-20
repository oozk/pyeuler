#!/usr/bin/env python3

import numpy as np
from numba import jit

@jit
def p139(L):

    seen   = np.empty(0, dtype=np.int64)
    def not_seen(e):
        for n in seen:
            if n == e: return False
        return True

    result = 0
    for u in range(2, int((L)**.5)+1):
        for v in range(1, u):
            p = 2*u**2 + 2*u*v             #perimeter
            if p < L:
                t  = (u**2 + v**2) / (((u**2 + v**2)**2 - 2*((u**2 - v**2) * 2*u*v))**.5)
                _t = int(t)
                if t - _t == 0:            #integer tiles
                    if not_seen(_t):       #seen this triangle?
                        seen = np.append(seen, _t)
                        result += int(L // p)
                        print(((u**2 - v**2), 2*u*v, (u**2 + v**2)), _t)
    # print(seen)
    return result

print(p139(1e8))
