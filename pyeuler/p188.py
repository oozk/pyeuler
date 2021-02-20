#!/usr/bin/env python3

def p188(a, k, m):
    p = a
    for i in range(1, k):
        p = pow(a, p, m)
    return p

print(p188(1777, 1855, int(1e8)))
