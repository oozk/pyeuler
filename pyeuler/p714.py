#!/usr/bin/env python3

###
# Problem 714
# https://projecteuler.net/problem=714
# ###
# Solution: O(n^2) time | O(1) space
###

from tqdm import tqdm

def D(k):
    result = 0
    for n in tqdm(range(1, k+1)):
        result += d(n)
    return result

def d(n):
    multipliers = lambda i : (int(bin(i)[2:]), int(''.join('1' if x == '0' else '0' for x in bin(i)[2:])))
    d_func      = lambda i, xy : sum(x[0] * x[1] for x in zip(multipliers(i), xy))

    i, k, l = 0, 0, 0
    found   = False
    min_r = float("inf")
    while True:
        i += 1
        if k < i and min_r < float("inf"):
            return min_r
        for y in range(0, 10):
            for x in range(0, 10):
                for j in range(2**(i-1), 2**i-1):
                    r = d_func(j, (x, y))
                    if 0 < r < min_r and r % n == 0:
                        min_r = r
                        k = i
                        break

def d2(n):
    i = 0
    isduodigit = lambda n : len(set([i for i in str(n)])) <= 2
    while True:
        i += 1
        r = n * i
        print(n, i)
        if isduodigit(r):
            return r


#print(d(290))
print(D(50000))
#245276790441833623865
