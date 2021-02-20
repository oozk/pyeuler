#!/usr/bin/env python3

from sympy import isprime
from itertools import product, combinations, permutations, groupby

def p111(n):

    primes    = [str(p) for p in sieve.primerange(10 ** (n-1), 10 ** n)]
    print(len(primes))

    ndigits   = lambda p, n: n == len(p) and len(p) != len(set(p))
    M         = lambda p, d: len(p) - len(p.replace(d, ''))
    shortlist = [[(p, d, M(p, str(d))) for d in range(0, 10) if M(p, str(d)) > 1]
                                       for p in primes if ndigits(p, n)]
    primes    = []

    ML        = lambda l: set((x[1], x[2]) for y in l for x in y)
    maxrepeat = lambda l: [(d, max(x[1] for x in ML(l) if x[0] == d)) for d in range(0, 10)]
    M_of_d    = list(maxrepeat(shortlist))
    results   = [(dd, sum(int(p) for x in shortlist for p, d, m in x if d == dd and m ==M))
                                                    for dd, M in M_of_d]
    print(results)

    return sum(x[1] for x in results)

def S(n, d):
    sum = 0
    for i in range(0, n + 1):
        digits = sorted(str(i) for i in range(0, 10) if i != d)
        for r in product(digits, repeat=i):
            for j in permutations(range(n), i):
                # print(j)
                num = str(d) * (n + 1)
                for k, l in enumerate(j):
                    num = num[:l] + r[k] + num[l+1:]
                    # print(num)
                print(num, r)
                if num == '38000000042':
                    print('stop')
                    return

    # print(digits)
    # r, sum    = 0, 0
    # while sum == 0:
    #     r    += 1
    #     pool =
    #     for p in pool:
    #         print(p)


S(10, 0)
# print(p111(10))
