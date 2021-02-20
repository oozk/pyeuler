#!/usr/bin/env python3

from math import gcd

def p071(l):
    n = lambda d: d * 3 // 7 - (1 if d % 7 == 0 else 0)
    d = [d for d in range(int(l)-7, int(l)+1)]
    d.sort(key=lambda d: n(d)/d)
    return n(d[-1]) // gcd(n(d[-1]), d[-1])

print(p071(1e6))
