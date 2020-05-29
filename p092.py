#!/usr/bin/env python3

###
# Problem 92
# https://projecteuler.net/problem=92
###

from tqdm import tqdm

def p092(n):
    c = 0
    for i in tqdm(range(2, n)):
        while True:
            s = 0
            for x in str(i):
                s += int(x) ** 2
            if s == 1:
                break
            if s == 89:
                c += 1
                break
            i = s
    return c

print(p092(int(1e7)))
