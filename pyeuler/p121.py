#!/usr/bin/env python3

from itertools import combinations
from functools import reduce
from operator  import mul
from math import floor

def p121(t):
    prob = 0
    blue = [1 / n for n in range(2, t+2)]
    for k in range(t//2 + 1, t+1):
        for c in combinations(range(t), k):
            prob += reduce(mul, [b if i in c else 1-b for i, b in enumerate(blue)], 1)
    return int(floor(1 / prob))

print(p121(15))
