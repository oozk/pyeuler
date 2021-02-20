#!/usr/bin/env python3

###
# Problem 95
# https://projecteuler.net/problem=95
###

import cProfile

def p095(limit):
    maximum, result = 0, None
    sumcache = divisorsum_eratosthenes(limit)
    for n in range(1, limit + 1):
        length, smallest = amicable_chain(n, limit, sumcache)
        if maximum < length:
            maximum, result = length, smallest
    return result

def amicable_chain(n, limit, sumcache):
    result = []
    while 0 < n < limit and n not in result:
        result.append(n)
        n = sumcache[n]
    if n in result:
        i = result.index(n)
        return (len(result[i:]), min(result[i:]))
    else:
        return (0, None)

def divisorsum_eratosthenes(n):
    sieve = [0] * int(n + 1)
    for i in range(1, int(n + 1)):
        for j in range(i * 2, int(n + 1), i):
            sieve[j] += i
    return sieve

cProfile.run('print(p095(1000000))')
