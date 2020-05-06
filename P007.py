#!/usr/bin/env python3

###
# Problem 7
# https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
###
# Solution: O((n^2)/2) time | O(n) space
###
import cProfile

def nthPrime(n):
    known_primes = (2, )
    count = len(known_primes)
    while count <= n - 1:
        known_primes += nextPrime(known_primes)
        count += 1
    return known_primes[-1]

def nextPrime(known_primes):
    m = known_primes[-1]
    while True:
        m += 1
        for x in known_primes:
            if m % x == 0:
                break
        else:
            return (m, )

cProfile.run('print(nthPrime(10001))')
