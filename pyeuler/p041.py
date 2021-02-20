#!/usr/bin/env python3

###
# Problem 41
# https://projecteuler.net/problem=41
###

import pickle

def p041():
    primes = load_pickle('primes_1e7.pkl')
    pandigits = dict((i, [str(j) for j in range(1, i + 1)]) for i in range(1, 10))
    pandigital = lambda x: sorted(str(x)) == pandigits[len(str(x))]
    return max(p for p in primes if pandigital(p))

def load_pickle(filename):
    kp_pkl = open(filename, 'rb')
    rpkl   = pickle.load(kp_pkl)
    kp_pkl.close()
    return rpkl

print(p041())
