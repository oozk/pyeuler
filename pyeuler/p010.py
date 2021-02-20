#!/usr/bin/env python3

###
# Problem 10
# https://projecteuler.net/problem=10
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
###
# Solution: O(n) time | O(n) space
###

import cProfile

def sum_Primes(max):
    known_primes = (2, )
    result = 0
    while known_primes[-1] <= max:
        result += known_primes[-1]
        known_primes += nextPrime(known_primes)
    return result

def nextPrime(known_primes):
    m = known_primes[-1]
    while True:
        m += 1
        for x in known_primes:
            if m % x == 0:
                break
        else:
            return (m, )

cProfile.run('print(sum_Primes(2e6))')
