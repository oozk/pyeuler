#!/usr/bin/env python3

###
# Problem 1
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###
# Solution: O(1) time | O(1) space
###
import cProfile

def sum_multiples_of_2_nums(N, n1, n2):

    if N<= 0 or n1 <= 0 or n2 <= 0 or \
       not (isinstance(N, int) and isinstance(n1, int) and isinstance(n2, int)):
        raise ValueError('All input values must be natural numbers.')

    multiples_Sum = lambda a, b : int(b * (a // b) * ((a // b) + 1) / 2)

    if n2 % n1 == 0 or n1 % n2 == 0:
        return multiples_Sum(N - 1, min(n1, n2))
    else:
        return multiples_Sum(N - 1, n1) + multiples_Sum(N - 1, n2) - multiples_Sum(N - 1, n1 * n2)

cProfile.run('print(sum_multiples_of_2_nums(int(1e12), int(3), int(5)))')
