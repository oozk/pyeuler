#!/usr/bin/env python3

from decimal import Decimal, getcontext

def p080(n, p):
    result = 0
    getcontext().prec = p + 2
    for i in range(n + 1):
        r = Decimal(i).sqrt()
        if len(str(r)) >= p:
            result += sum(int(x) for x in list(str(r)[:p + 1].replace('.','')))
    return(result)

print(p080(100, 100))
