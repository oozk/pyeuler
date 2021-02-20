#!/usr/bin/env python3

def p119():

    digitsum = lambda d, n: sum(int(x) for x in list(str(n))) == d
    a = [(d ** p, d, p) for p in range(2, 15) for d in range(2, 100) if digitsum(d, d ** p)]
    a.sort()
    return a[29][0]

print(p119())
