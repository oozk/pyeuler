#!/usr/bin/env python3

from math import floor

def p197(N):
    f      = lambda x: floor(2 ** (30.403243784 - x ** 2)) / 1e9
    result = 0
    u0     = f(-1)
    for n in range(1, int(N+1)):
        u1 = f(u0)
        u  = round(u0+u1, 9)
        if result == u:
            return result
        else:
            result = u
        u0 = u1

    return result

print(p197(1e12))
