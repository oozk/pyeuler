#!/usr/bin/env python3

from itertools import permutations

def p068(n, d):

    pool   = range(1, 2 * n + 1)
    gonidx = [(i, i + n, i + n + 1 if i + 1 < n else i + 1) for i in range(n)]

    gonify = lambda p: [(p[i], p[j], p[k]) for (i, j, k) in gonidx]
    valid  = lambda s: len(set(sum(x) for x in s)) == 1 and min(x[0] for x in s) == s[0][0]
    merge  = lambda s: ''.join(str(x) for x in s)

    solutions = [gonify(p) for p in permutations(pool) if valid(gonify(p))]

    result = max(int(merge(s)) for s in [[merge(x) for x in s] for s in solutions] \
                                                                    if len(merge(s)) == d)

    return result

print(p068(3, 9))
print(p068(4, 12))
print(p068(5, 16))
