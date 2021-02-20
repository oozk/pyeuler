#!/usr/bin/env python3

###
# Problem 87
# https://projecteuler.net/problem=87
###

def p087(n):
    primes = sieve_of_eratosthenes(n ** 0.5)
    p2 = [p ** 2 for p in primes]
    p3 = [p ** 3 for p in primes if p ** 3 < n]
    p4 = [p ** 4 for p in primes if p ** 4 < n]
    return len(set(a + b + c for a in p2 for b in p3 for c in p4 if a + b + c < n))

def sieve_of_eratosthenes(n):
    primes = []
    sieve = [True] * int(n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, int(n+1), i):
                sieve[j] = False
    primes = set(p for p, bool in enumerate(sieve) if bool)
    return primes

print(p087(5e7))
