#!/usr/bin/env python3

from itertools import product
from math import comb
from operator import mul
from functools import reduce

def p824():

    R = range(7)
    D = {n:comb(6, n) for n in R}

    answer = 0
    for p in product(R, R, R, R, R, R):
        if sum(p) == 12:
            print(p, [D[n] for n in p], reduce(mul, [D[n] for n in p], 1))
            answer += reduce(mul, [D[n] for n in p], 1)

    return answer

print(p824())

1251677700
