#!/usr/bin/env python3

###
# Problem 74
# https://projecteuler.net/problem=74
###

from math import factorial
from itertools import permutations

def p074():
    factorials = dict((str(i), factorial(i)) for i in range(0, 10))
    chain_link = lambda n: sum(factorials[i] for i in str(n))
    result = 0
    for i in range(1, 1000000):
        chain = [i]
        n = chain_link(i)
        while n not in chain:
            chain.append(n)
            n = chain_link(n)
        if len(chain) == 60: result += 1
    return result

def p074_opt():
    factorials = dict((str(i), factorial(i)) for i in range(0, 10))
    chain_link = lambda n: sum(factorials[i] for i in str(n))
    list2int = lambda l: int(''.join(l))
    perm = lambda n, c: ((list2int(p), c) for p in permutations(str(n)) if p[0] != '0')
    checked = {}
    for i in range(1, 1000000):
        if i in checked: continue
        chain = [i]
        n = chain_link(i)
        while n not in chain:
            chain.append(n)
            n = chain_link(n)
        checked.update(perm(i, len(chain)))
    return sum(1 for k in checked if checked[k] == 60)

# print(p074())
print(p074_opt())
