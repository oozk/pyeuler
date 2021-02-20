#!/usr/bin/env python3

###
# Problem 9
# https://projecteuler.net/problem=9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ###
# Solution: O(n^2) time | O(1) space
###

import cProfile
import operator
from functools import reduce

def special_pythagorean_triplet(N):
    pool = ((a, b, 1000-a-b) for a in range(1, N - 1) for b in range(a, N - 1) if (a**2 + b ** 2 == (1000-a-b) ** 2))
    for x in pool:
        return reduce(operator.mul, x, 1), x

cProfile.run('print(special_pythagorean_triplet(1000))')
