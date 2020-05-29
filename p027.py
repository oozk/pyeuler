#!/usr/bin/env python3

###
# Problem 27
# https://projecteuler.net/problem=27
###

def p027():
    is_prime = sieve_of_eratosthenes(1e5)
    coefficients = ((i, j) for i in range(-999, 1000) for j in range(-1000, 1001))
    maximum, result = 0, None
    for (a, b) in coefficients:
        n = 0
        while is_prime[n ** 2 + a * n + b]:
            n += 1
            if maximum < n: maximum, result = n, a * b
    return result

def sieve_of_eratosthenes(n):
    sieve = [True] * int(n + 1)
    sieve[0] = sieve[1] = 1
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * i, int(n + 1), i):
            sieve[j] = False
    return sieve

print(p027())
