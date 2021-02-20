#!/usr/bin/env python3

from sympy import isprime

def p146(L):
    p      = [1, 3, 7, 9, 13, 27]
    e      = [i for i in range(1, p[-1]+1, 2) if i not in p]
    test   = lambda x: all(isprime(x**2 + i) for i in p) and \
                       not any(isprime(x**2 + i) for i in e)
    return sum(70*n+x for n in range(int(L/70)) for x in [10, 60] if test(70*n+x))

print(p146(15e7))
