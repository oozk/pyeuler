#!/usr/bin/env python3

from scipy.interpolate import lagrange

def p101(d):
    u       = lambda n: sum((-n) ** p for p in range(d+1))
    x, y    = [x for x in range(1, d+1)], [u(x) for x in range(1, d+1)]

    sumFITs = 1
    for i in range(2, d+1):
        OP  = lagrange(x[:i], y[:i])
        FIT = lambda x: int(round(OP(x + 1)))
        sumFITs += FIT(i)

    return sumFITs

print(p101(10))
