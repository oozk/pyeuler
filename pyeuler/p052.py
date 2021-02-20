#!/usr/bin/env python3

###
# Problem 52
# https://projecteuler.net/problem=52
###

def p052():
    i = 0
    while True:
        i += 1
        if same_digits(i):
            return i

def same_digits(n):
    digits = lambda i : ''.join(sorted([a for a in str(i)]))
    x = digits(n)
    for i in range(2, 7):
        if x != digits(n * i):
            return False
    return True

print(p052())
