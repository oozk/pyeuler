#!/usr/bin/env python3

###
# Problem 88
# https://projecteuler.net/problem=88
# ###
# Solution: O(n^2) time | O(n) space
###

import cProfile
import operator
from functools import reduce

def problem_88(L):
    N = {k : 2* k for k in range(2, L + 1)}
    k = 2
    N[2] = 4
    for n in range(N[k], 2 * L + 1):
        factors = []
        list_factors(n, 2, 1, tuple(), factors)
        for j in factors:
            k = n - sum(j) + len(j)
            if 2 <= k <= L and N[k] > n:
                print(k, n, j)
                N[k] = n

    return sum(set(N.values()))

def list_factors(n, start_factor, current_factor, result, factors):

    if current_factor > n or start_factor > n:
        return

    if current_factor == n:
        factors.append(result)
        return

    for i in range(start_factor, n + 1):
        if current_factor * i > n:
            break
        if n % i == 0:
            result += (i, )
            list_factors(n, i, current_factor * i, result, factors)
            result = result[:-1]

print(problem_88(12000))
