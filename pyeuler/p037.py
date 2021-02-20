#!/usr/bin/env python3

###
# Problem 37
# https://projecteuler.net/problem=37
###

import pickle

def p037():
    primes = load_pickle('known_primes.pkl')
    sieve = [False] * (primes[-1] + 1)
    for i in primes:
        sieve[i] = True

    left_truncatable = lambda p : all(sieve[int(p[i:])] for i in range(len(p))) and len(p) > 1
    right_truncatable = lambda p : all(sieve[int(p[:-i])] for i in range(1, len(p))) and len(p) > 1
    return sum(p for p in primes if left_truncatable(str(p)) and right_truncatable(str(p)))

def load_pickle(filename):
    kp_pkl = open(filename, 'rb')
    rpkl   = pickle.load(kp_pkl)
    kp_pkl.close()
    return rpkl


print(p037())
