#!/usr/bin/env python3

###
# Problem 5
# https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
###
# Solution: O(n) time | O(1) space
###
import cProfile

def smallest_multiple(from_num, to_num):
    r = 1
    for i in range(from_num, to_num + 1):
        if r % i != 0:
           for j in prime_factors(i):
               if (r * j) % i == 0:
                   r *= j
                   break
    return r

def prime_factors(n, start=2):
    pool = range(start, int(n ** 0.5) + 1)
    factor = next((x for x in pool if (n % x == 0)), None)
    return ([factor] + prime_factors(n // factor, factor) if factor else [n])


cProfile.run('print(smallest_multiple(1, 20))')
