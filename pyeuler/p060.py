#!/usr/bin/env python3

###
# Problem 60
# https://projecteuler.net/problem=60
# ###
# Solution: O(n) time | O(n) space
###

import math
import pickle
import cProfile

def problem_60(m, filename):
    known_pairs  = load_pickle(filename)
    kp_reduced = load_pickle(filename)

    known_pair_keys = sorted(kp_reduced)
    for i in kp_reduced:
        kp_reduced[i] = list(set(kp_reduced[i]) & set(known_pair_keys))

    known_groups = []
    for i in kp_reduced:
        for j in kp_reduced[i]:
            intersection = list(set(kp_reduced[i]) & set(kp_reduced[j]))
            prime_group = []
            if len(intersection) > 0:
                intersection.sort()
                prime_group.append(i)
                prime_group.append(j)
                for x in intersection:
                    if search_pairs(x, prime_group, known_pairs):
                        prime_group.append(x)
            if len(prime_group) > 2:
                known_groups.append(prime_group)

    best = (float('inf'), 0)
    solutions = []
    for g in known_groups:
        if len(g) >= m:
            g.sort()
            pick = [g[i] for i in range(0, m)]
            solutions.append((sum(pick), pick))
            if best[0] > sum(pick):
                best = (sum(pick), pick)

    print(best)
    solutions.sort()
    print(solutions)

def search_pairs(x, g, known_pairs):
    for j in g:
        if x not in known_pairs[j]:
            return False
    else:
        return True

def pickle_primes(n):
    known_primes = nthPrime(n)
    kp_pkl       = open('known_primes.pkl', 'wb')
    pickle.dump(known_primes, kp_pkl)
    kp_pkl.close()

def pickle_pairs(start, end, filename):
    known_primes = load_pickle('known_primes.pkl')
    known_pairs  = prime_pairs(known_primes, known_primes, start, end)
    kp_pkl       = open(filename, 'wb')
    pickle.dump(known_pairs, kp_pkl)
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

def prime_pairs(list_search, known_primes, start, end):
    list_pairs, result = [], dict()
    isprime = lambda i, j : is_prime(int(str(list_search[i]) + str(list_search[j])), known_primes) and is_prime(int(str(list_search[j]) + str(list_search[i])), known_primes)
    for i in range(start, end):
        print(i)
        for j in range(i, end):
            if isprime(i, j):
                list_pairs.append(list_search[j])
        else:
            if len(list_pairs) >= 1:
                result[list_search[i]] = list_pairs
            list_pairs = []
    return result

def nthPrime(n):
    known_primes = (2, )
    count = len(known_primes)
    while count <= n - 1:
        known_primes += nextPrime(known_primes)
        count += 1
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

pickle_primes(30000)
pickle_pairs(1, 2000, 'known_pairs_2000.pkl')
cProfile.run('problem_60(5, "known_pairs_2000.pkl")')
