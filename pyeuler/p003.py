#!/usr/bin/env python3

###
# Problem 3
# https://projecteuler.net/problem=3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
###
# Solution: O(sqrt(n)) time | O(1) space
###
import cProfile

def largest_prime_factor(n):
    return int(max(prime_factors(n)))

def prime_factors(n, start=2):
    pool = range(start, int(n ** 0.5) + 1)
    factor = next((x for x in pool if (n % x == 0)), None)
    return ([factor] + prime_factors(n / factor, factor) if factor else [n])

cProfile.run('print(largest_prime_factor(600851475143))')
