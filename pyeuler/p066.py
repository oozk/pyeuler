#!/usr/bin/env python3

###
# Problem 66
# https://projecteuler.net/problem=66
###
import sympy as sy

def p066(lim):

    solutions = []

    for D in range(2, lim + 1):



    # avoid = [73, 94, 97]
    # for D in range(2, lim + 1):
    #     y = 0
    #     if D ** .5 - int(D ** .5) == 0:
    #         continue
    #     if D in avoid:
    #         continue
    #     while True:
    #         y += 1
    #         x = (1 + D * (y ** 2)) ** .5
    #         print(D, x, y)
    #         if round(x, 6) - int(x) == 0:
    #             solutions.append((D, int(x)))
    #             break
    #
    # print(solutions)

p066(100)
