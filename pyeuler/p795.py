#!/usr/bin/env python3

from math import gcd
from sympy import isprime, factorint

def p795(N):
    k      = N // 2
    result = 1 - k**2

    for p in range(1, k+1):
        print(p)
        if p != 2 and isprime(p):
            result += (2*p-1)
        else:
            F = factorint(2*p)
            x = 1
            for q in F.keys():
                x *= (q ** round(F[q] // 2, 0))
            for i in range(1, (2*p // x)+1):
                result += x * (-1)**i * gcd(i**2, 2*p)

    return result

print(p795(12345678))
