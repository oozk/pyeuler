#!/usr/bin/env python3

###
# Problem 51
# https://projecteuler.net/problem=51
###

import pickle
from itertools import permutations
import cProfile
from tqdm import tqdm
import time

def p051(n):

    primes = load_pickle('primes_1e7.pkl')

    repeats   = lambda p: ((x, i) for i, x in enumerate(p) if p.count(x) > 1)
    repeatidx = lambda p: ([i[1] for i in repeats(p) if i[0] == j] \
                                 for j in set(i[0] for i in repeats(p)))

    key       = lambda p, r, d: ''.join(d if i in r else j for i, j in enumerate(p))

    pool = dict()
    for p in primes:
        q  = str(p)
        for r in repeatidx(q):
            for i in range(2, len(r) +1):
                for m in permutations(r, i):
                    k = key(q, m, '_')
                    try:
                        pool[k].add(p)
                        if len(pool[k]) == n:
                            print(k, sorted(pool[k]))
                            return min(pool[k])
                    except:
                        pool[k] = set()
                        pool[k].add(p)


def load_pickle(filename):
    kp_pkl = open(filename, 'rb')
    rpkl   = pickle.load(kp_pkl)
    kp_pkl.close()
    return rpkl

print(p051(6))
print(p051(7))
print(p051(8))


def p051_1(n):

    primes = load_pickle('primes_1e7.pkl')

    samedigit = lambda p, m: len(set(p[i] for i, j in enumerate(m) if j == '1')) == 1
    key       = lambda p, m, d: ''.join(p[i] if j!='1' else d for i, j in enumerate(m))

    pool = dict()
    for p in primes:
        q  = str(p)
        lp = len(q)
        lq = len(set(q))
        if lq < lp:
            for m in range(1 << lp):
                mask = bin(m)[2:]
                if 1 < mask.count('1') <= lp - lq + 1:
                    mask = mask.zfill(lp)
                    if samedigit(q, mask):
                        k = key(q, mask, '_')
                        try:
                            pool[k].add(p)
                            if len(pool[k]) == n:
                                print(k, sorted(pool[k]))
                                return min(pool[k])
                        except:
                            pool[k] = set()
                            pool[k].add(p)
