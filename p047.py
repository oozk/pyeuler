#!/usr/bin/env python3

###
# Problem 47
# https://projecteuler.net/problem=47
###

def p047(s, n):
    i = 0
    while True:
        s += 1
        i = i + 1 if len(set(prime_factors(s))) == n else 0
        if i == n:
            return s - n + 1

def prime_factors(n, start=2):
    pool = range(start, int(n ** 0.5) + 1)
    factor = next((x for x in pool if (n % x == 0)), None)
    return ([factor] + prime_factors(n // factor, factor) if factor else [n])

print(p047(646, 4))
