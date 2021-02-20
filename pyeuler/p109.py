#!/usr/bin/env python3

from itertools import product

def p109(LIMIT):

    R = {'S':1, 'D':2, 'T':3}
    D = {x + str(y): R[x] * y for x in R for y in range(1, 21)}
    D['S25'], D['D25'] = 25, 50

    checkout = lambda s: sum(D[x] for x in s) < LIMIT and s[-1][:1] == 'D'

    result   = set(' '.join(s) if i <= 2 else \
                   ' '.join(sorted(s[:2])) + ' ' + s[-1] \
                   for i in range(1, 4) \
                   for s in product(D.keys(), repeat=i) \
                   if checkout(s))

    print(sorted(result))
    return len(result)

print(p109(100))
