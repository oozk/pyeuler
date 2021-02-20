#!/usr/bin/env python3

def p063_2():
    count = 0
    for b in range(1, 10):
        for p in range(1, 23):
            if len(str(b ** p)) == p:
                count += 1
    return count

print(p063_2())

from math import log10, floor
print(sum([floor(1/(1-log10(a))) for a in range(1,9+1)]))
