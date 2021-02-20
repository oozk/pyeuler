#!/usr/bin/env python3

###
# Problem 3
# https://projecteuler.net/problem=36
# ###
# Solution: O(n) time | O(1) space
###

import cProfile

def problem_36_bf(N):
    ispalindromic = lambda s : s == s[::-1]
    return sum(i for i in range(1, N, 2) if ispalindromic(str(i)) and ispalindromic(bin(i)[2:]))

def problem_36_opt(N):
    ispalindromic = lambda s : s == s[::-1]
    return sum(i for i in make_odd_palindromes(N) if ispalindromic(bin(i)[2:]))

def make_odd_palindromes(N):
    for i in range(1,  10 ** int(len(str(N)) / 2)):
        n = int(str(i)[:-1] + str(i)[::-1])
        if n < N and n % 2 != 0:
            yield n
        n = int(str(i) + str(i)[::-1])
        if n < N and n % 2 != 0:
            yield n


# cProfile.run('print(problem_36_bf(1000000))')
cProfile.run('print(problem_36_opt(1000000))')
