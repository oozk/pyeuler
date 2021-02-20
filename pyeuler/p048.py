#!/usr/bin/env python3

###
# Problem 48
# https://projecteuler.net/problem=48
###

def p048():
    return str(sum(i ** i for i in range(1, 1001)))[-10:]

print(p048())
