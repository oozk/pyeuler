#!/usr/bin/env python3

###
# Problem 4
# https://projecteuler.net/problem=46
###

known_primes = (1, 2, )

def p046():
    i = 135
    while True:
        i += 2
        nthPrime(i)
        if not goldbach(i):
            return i

def goldbach(n):
    global known_primes
    if n in known_primes:
        return True
    for i in known_primes:
        r = (n - i) / 2.
        if r > 0:
            if (r - int(r)) == 0 and ((r ** 0.5) - int(r ** 0.5)) == 0:
                return True
    return False

def nthPrime(n):
    global known_primes
    while known_primes[-1]  <= n:
        known_primes += nextPrime(known_primes)
    return known_primes[-1]

def nextPrime(known_primes):
    m = known_primes[-1]
    while True:
        m += 1
        for x in known_primes:
            if x > 1 and m % x == 0:
                break
        else:
            return (m, )

print(p046())
