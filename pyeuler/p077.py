#!/usr/bin/env python3

###
# Problem 77
# https://projecteuler.net/problem=77
###

def p077():
    n = 1
    while True:
        if countways(n) > 5000: return n
        n += 1

def countways(n):
    ways = [1] + [0] * n
    primes = sieve_of_eratosthenes(n)
    for p in primes:
        for i in range(n - p + 1):
            ways[i + p] += ways[i]
    return ways[n]

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

print(p077())
