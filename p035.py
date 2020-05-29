#!/usr/bin/env python3

###
# Problem 35
# https://projecteuler.net/problem=35
# ###
# Solution: O(n) time | O(n) space
###

import math
import pickle
import cProfile

def p035():
    primes = load_pickle('known_primes.pkl')
    pool = {}
    result = []
    key = lambda n : ''.join(sorted(str(n)))
    rotations = lambda r, pool: all(x in pool for x in r)
    for p in primes:
        if p >= 1e6: break
        try: pool[key(p)] += (p, )
        except: pool[key(p)] = (p, )
    for k in pool:
        if len(pool[k]) >= 1:
            for p in pool[k]:
                s = str(p)
                r = [p]
                for i in range(len(str(p))):
                    s = s[-1] + s[:-1]
                    r.append(int(s))
                if rotations(r, pool[k]):
                    result += r
    print(sorted(set(result)))
    return len(set(result))

def pickle_primes(n):
    known_primes = getPrimes(n)
    kp_pkl       = open('known_primes.pkl', 'wb')
    pickle.dump(known_primes, kp_pkl)
    kp_pkl.close()

def load_pickle(filename):
    kp_pkl = open(filename, 'rb')
    rpkl   = pickle.load(kp_pkl)
    kp_pkl.close()
    return rpkl

def is_prime(n, known_primes):
    if n in known_primes:
        return True
    limit = int(n ** 0.5)
    for i in known_primes:
        if i <= limit and n % i == 0:
            return False
    else:
        return True

def getPrimes(n):
    known_primes = (2, )
    while known_primes[-1] <= n:
        known_primes += nextPrime(known_primes)
    return known_primes

def nextPrime(known_primes):
    m = known_primes[-1]
    while True:
        m += 1
        for x in known_primes:
            if m % x == 0:
                break
        else:
            return (m, )

pickle_primes(10000000)
# print(p035())
