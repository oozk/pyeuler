#!/usr/bin/env python3

###
# Problem 78
# https://projecteuler.net/problem=78
###

from itertools import *

def pentagonal(n):
    return n*(3*n - 1) / 2

partitions = {}
generalized_pentagonals = sorted(map(pentagonal, list(range(-250, 250))))[1:]
def partition(n):
    if n <= 1: return 1
    if n not in partitions:
        signs = cycle([1, 1, -1, -1])
        pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
        partitions[n] = sum(sign * partition(n - p) for sign, p in zip(signs, pentagonals))

    return partitions[n]

def main():
    print(next((n for n in count(0) if partition(n) % 1000000 == 0)))

if __name__ == "__main__": main()
# pentagonal = lambda n: n * (3 * n - 1) / 2
# generalized_pentagonals = sorted(map(pentagonal, list(range(-250, 250))))[1:]
#
# def p078():
#     print(generalized_pentagonals)
#     print(next((n for n in count(0) if partition(n) % 1000000 == 0)))
#
# def partition(n):
#     partitions = {}
#     if n <= 1: return 1
#     if n not in partitions:
#         signs = cycle([1, 1, -1, -1])
#         pentagonals = takewhile(lambda p: p <= n, generalized_pentagonals)
#         partitions[n] = sum(sign * partition(n - p) for sign, p in zip(signs, pentagonals))
#     return partitions[n]
#
# p078()

# def p078():
#     n = 0
#     while True:
#         n += 1
#         r = ways(n)
#         print(n, r, )
#         if r % 1000000 == 0:
#             return n
#
# def ways(n):
#     coins = range(1, n + 1)
#     ways = [1] + [0] * n
#     for c in coins:
#         for i in range(n - c + 1):
#             ways[i + c] += ways[i]
#     return ways[n]
#
# print(p078())
