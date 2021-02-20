#!/usr/bin/env python3

###
# Problem 123
# https://projecteuler.net/problem=123
###

import pickle

def p123(target):
    primes      = load_pickle('primes_1e7.pkl')[1:]
    sqremainder = lambda p, n, psq: (pow(p + 1, n, psq) + pow(p - 1, n, psq)) % psq
    ptarget     = target ** .5
    for i, p in enumerate(primes, 2):
        if p < ptarget: continue
        if sqremainder(p, i + 1, p ** 2) > target:
            return i + 1

def load_pickle(filename):
    kp_pkl = open(filename, 'rb')
    rpkl   = pickle.load(kp_pkl)
    kp_pkl.close()
    return rpkl

print(p123(1e10))
