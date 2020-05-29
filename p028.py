#!/usr/bin/env python3

###
# Problem 28
# https://projecteuler.net/problem=28
###

def p028(n):
    value = 1
    result = value
    for i in range(3, n+1, 2):
        for j in range(4):
            value += i - 1
            result += value
    return result

print(p028(1001))
