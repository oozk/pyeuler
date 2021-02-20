#!/usr/bin/env python3

from itertools import product
from math import factorial
from operator import mul
from functools import reduce

def p491():

    div11    = lambda p: (90 - 2*sum(map(mul, p, range(10)))) % 11 == 0
    even_set = (p for p in product(range(3), repeat=10) if sum(p) == 10 and div11(p))

    result   = 0
    for p in even_set:
        odds    = factorial(10) // reduce(mul, [factorial(2-x) for x in p], 1)
        evens   = (10-p[0]) * factorial(9) // reduce(mul, [factorial(x) for x in p], 1)
        result += odds * evens
    return result

print(p491())

def p491_2():
    return sum((10-p[0]) * 10 * (362880 **2) // (2**(10-p.count(1))) \
                for p in product(range(3), repeat=10) \
                if sum(p) == 10 and (sum(p[i] * i for i in range(10))-1) % 11 == 0 \
               )

print(p491_2())

print(factorial(10), factorial(9))
