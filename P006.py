#!/usr/bin/env python3

###
# Problem 6
# https://projecteuler.net/problem=6
# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2=55^2=3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# ###
# Solution: O(1) time | O(1) space
###
import cProfile

def sum_square_difference(n):
    m = n ** 2 + n
    return m ** 2 / 4 - m * (2 * n + 1) / 6
    # alternative in O(n) time: sum(i ** 3 - i ** 2 for i in xrange(1, n + 1))

cProfile.run('print(sum_square_difference(1000000000000000000000000))')
