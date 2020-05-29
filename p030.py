#!/usr/bin/env python3

###
# Problem 30
# https://projecteuler.net/problem=30
###

def p030(n):
    fifth_power = lambda x : x == sum(int(y) ** 5 for y in str(x))
    return sum(i for i in range(2, n) if fifth_power(i))

print(p030(1000000))
