#!/usr/bin/env python3

from math import gcd

def p073(l):
    return len(set((k//gcd(k, d), d//gcd(k, d)) for d in range(2, l+1) for k in range(d//3, d//2+1) if 2*k< d <3*k))

print(p073(12000))
