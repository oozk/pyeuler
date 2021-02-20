#!/usr/bin/env python3

import cProfile
from itertools import combinations, product

def p103(A_, depth):

    nextset    = lambda A: [A[len(A)//2]] + [A[len(A)//2] + x for x in A]
    specialsum = lambda A: all(sum(B) > sum(C) if len(B) > len(C) else
                               sum(B) < sum(C) if len(B) < len(C) else
                               sum(B) != sum(C) for i in range(1, len(A))
                                                for j in range(1, len(A) - i + 1)
                                                for B in combinations(A, i)
                                                for C in combinations(diff(A, B), j)
                                                if i >= j)
    increasing= lambda A: sorted(A) == A
    positive  = lambda A: min(A) > 0
    increment = lambda A, d: [A[i] + d[i] for i in range(len(A))]
    searchpool= [-x for x in reversed(range(0, depth + 1))] + [x for x in range(1, depth + 1)]
    stringify = lambda A: ''.join(str(x) for x in A)


    A         = nextset(sorted(A_))
    minimum   = sum(A)
    solution  = A
    count     = 1
    print('Pass %s: %s Sum: %s' % (count, stringify(A), sum(A)))

    for d in product(searchpool, repeat=len(A)):
        A_ = increment(A, d)
        if not increasing(A_) and not positive(A_): continue
        if specialsum(A_):
            if minimum > sum(A_):
                count += 1
                print('Pass %s: %s Sum: %s' % (count, stringify(A_), sum(A_)))
                minimum = sum(A_)
                solution = A_

    return stringify(solution)

def diff(A, B):
    C = A.copy()
    for b in B:
        if b in C:
            C.remove(b)
    return C


cProfile.run('print(p103([11, 18, 19, 20, 22, 25], 2))')
