#!/usr/bin/env python3

###
# Problem 49
# https://projecteuler.net/problem=49
###

def p049(n):
    permkey = lambda x : ''.join(sorted(str(x)))
    pool = {}
    primes = getPrimes(int('9' * n))
    for p in primes:
      if p > 10 ** (n-1) and p <= int('9' * n):
          try:
              pool[permkey(p)] += (p, )
          except:
              pool[permkey(p)] = (p, )
    for x in pool:
        if len(pool[x]) > 2:
            for i in range(0, len(pool[x])-2):
                for j in range(i + 1, len(pool[x])-1):
                    for k in range(j + 1, len(pool[x])):
                        if pool[x][k] - pool[x][j] == pool[x][j] - pool[x][i]:
                            print(pool[x][i], pool[x][j], pool[x][k])

def getPrimes(n):
    known_primes = (2, )
    while known_primes[-1]  <= n:
      known_primes += nextPrime(known_primes)
    return known_primes[:-1]

def nextPrime(known_primes):
    m = known_primes[-1]
    while True:
        m += 1
        for x in known_primes:
            if m % x == 0:
                break
        else:
            return (m, )

p049(6)
