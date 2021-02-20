#!/usr/bin/env python3

from itertools import permutations
from sympy import isprime

def partitions(n):
    if n == 0:
        yield []
        return

    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def p118():
    setconfig = list(partitions(9))
    shortlist = []
    for c in permutations(range(1, 10), 9):
        if len(set(c)) == 9:
            p = ''.join(str(x) for x in c)
            for s in setconfig:
                r = sorted([int(p[sum(s[:i]):sum(s[:i+1])]) for i in range(0, len(s))])
                if all(isprime(i) for i in r):
                    shortlist += [r]
    result = 0
    last   = []
    for r in sorted(shortlist):
        if last != r:
            result += 1
            last    = r
    return result




    # pandigital = lambda p, l, e: len(set(str(p))) == l and \
    #                                  all(str(k) not in str(p) for k in [0] + e)
    # primes     = lambda l, e: [p for p, b in enumerate(sieve[int(10**(l-1)-1):int(10 ** (l))]) \
    #                            if b and pandigital(p, l, e)]
    # sieve = np.full(int(1e9+1), True, dtype=bool)
    # sieve[0] = sieve[1] = False
    # for i in range(2, int(1e9 ** .5) + 1):
    #     if sieve[i]: sieve[i * i :: i] = False

    # result = 0
    # for s in setconfig:
    #     e = []
    #     count = 0
    #     for l in s:
    #         p =



    #
    # results = []
    # for p in primes:
    #     print(p, list(nextprime(p)))

    #
    #
    # pandigits= set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # digits   = [str(x) for x in range(1, 10)]
    # allprime = lambda p: all(isprime(int(''.join(x))) for x in p)
    # primes   = lambda r: [int(x) for x in r]
    # pandigit = lambda p: ''.join(sorted(str(p))) == '123456789'
    #
    # results  = []
    # for p, b in enumerate(sieve):
    #     if not b: continue
    #     if p >= 1e6): continue
    #     if not pandigit(p): continue
    #
    #
    #     for s in range(0, 5):
    #         for r in partitions(str(p), s):
    #             print(p, s, r)
    #             if allprime(r):
    #                 results += [primes(r)]
    #
    # return len(results)

# def buildset(primes, outlist):
#
#
# def partitions(n, s):
#
#     if s == 0: return {(n, )}
#     output = set()
#     parts = list(range(0, len(n) - (len(n) + 1) // (s + 1)))
#
#         c = sorted(c)
#         c += (len(n) - 1, )
#         result = []
#         result += {n[:c[0]+1]}
#         for i in range(0, len(c)-1):
#             result += {n[c[i] + 1:c[i + 1]+1]}
#         yield result

print(p118())
