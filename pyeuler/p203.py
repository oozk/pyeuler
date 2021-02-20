#!/usr/bin/env python3

def pascal_triangle(n):
    p      = [[1]]
    while len(p) < n:
        r  = p[-1]
        p += [[1] + [r[i] + r[i+1] for i in range(len(r)-1)] + [1]]
    return p

def p203(n):
    sqfree = lambda x: not(x%4==0 or any(x%(i**2)==0 for i in range(3, int(x**.5)+1, 2)))
    return sum(x for x in set(x for p in pascal_triangle(n) for x in p) if sqfree(x))

print(p203(51))
