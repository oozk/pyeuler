#!/usr/bin/env python3

from math import gcd

def p243(n, d):

    primes     = [x for x in range(2, 101) if all(x%y != 0 for y in range(2, int(x**.5)+1))]
    # totient = lambda x: sum(1 for y in range(1, x) if gcd(x, y) == 1)

    result      = 1
    resiliance  = 1
    for p in primes:
        result *= p
        resiliance = resiliance * p - resiliance
        if resiliance / result < n / d:
            break

    for i in range(1, p+1):
        if (resiliance * i) / (result * i - 1) < n / d:
            result *= i
            return result


print(p243(4, 10))
print(p243(15499, 94744))
