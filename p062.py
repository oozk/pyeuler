#!/usr/bin/env python3

###
# Problem 62
# https://projecteuler.net/problem=62
###

import cProfile

def p062(target):
    n, cubes = 0, {}
    while True:
        n += 1
        k = ''.join(sorted(str(n ** 3)))
        try:
            cubes[k] += (n, )
            if len(cubes[k]) == target:
                return min(cubes[k]) ** 3
        except: cubes[k] = (n, )


cProfile.run('print(p062(5))')

# cProfile.run('print(p062(40))')
