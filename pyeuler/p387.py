#!/usr/bin/env python3

from math import log, floor
from sympy import isprime

def p387(l):
    primeend = [1, 3, 7, 9]
    harshad  = [(n, n) for n in range(1, 10)]
    primes   = []
    cnt      = floor(log(l, 10)) - 2
    while cnt > 0:
        harshad  = [(10*n+k, m+k) for n, m in harshad \
                      for k in range(10) if (10*n+k)%(m+k) == 0]
        primes  += [10*n+k for n, m in harshad for k in primeend \
                      if isprime(10*n+k) and isprime(n//m) and 10*n+k < l]
        cnt     -= 1
    print(primes)
    return sum(primes)

print(p387(1e14))
