#!/usr/bin/env python3

###
# Problem 97
# https://projecteuler.net/problem=97
###

def p097():
    return (28433 * pow(2, 7830457, int(1e10)) +1) % int(1e10)

print(p097())
