#!/usr/bin/env python3

###
# Problem 75
# https://projecteuler.net/problem=75
###

from math import gcd

def p075(n):
    pool = {}
    for s in range(3, int(n ** 0.5) + 1, 2):
        for t in range(s - 2, 0, -2):
            if gcd(s, t) == 1:
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2
                l = a + b + c
                if l <= n:
                    sides = (a, b, c)
                    try:
                        pool[l] += sides
                    except:
                        pool[l] = sides

    ways = [0] * (n + 1)
    for k in pool:
        sigma = sum(pool[k])
        for i in range(sigma, len(ways), sigma):
            ways[i] += 1

    result = ways.count(1)
    return str(result)
    # print(pool)
    # return sum(1 for d in pool if len(pool[d]) == 1)

print(p075(1500000))
