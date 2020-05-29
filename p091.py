#!/usr/bin/env python3

###
# Problem 91
# https://projecteuler.net/problem=91
###

from math import acos, pi

def p091_1(x_lim, y_lim):
    P = [(x, y) for x in range(x_lim + 1) for y in range(y_lim + 1) if (x, y) != (0, 0)]
    vertices = (((0, 0), p, q) for p in P for q in P if p != q)
    return sum(1 for (o, p, q) in vertices if right_triangle(o, p, q)) // 2

def right_triangle(o, p, q):
    dist = lambda p, q: ((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
    aa, bb, cc = sorted([dist(o, p), dist(o, q), dist(p, q)])
    return aa + bb == cc

print(p091_1(50, 50))

def p091_2(x_lim, y_lim):
    P = [(x, y) for x in range(x_lim + 1) for y in range(y_lim + 1) if (x, y) != (0, 0)]
    vertices = (((0, 0), p, q) for p in P for q in P if p != q)
    return sum(1 for v in vertices if largest_angle(v) == 90.000) // 2

def largest_angle(v):
    distance = lambda v1, v2: ((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2) ** 0.5
    angle = lambda a, b, c: acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) * 180 / pi
    largest = lambda a, b, c: round(max(angle(a, b, c), angle(a, c, b), angle(b, c, a)), 3)
    try:
        return largest(distance(v[0], v[1]), distance(v[0], v[2]), distance(v[1], v[2]))
    except:
        return None

# print(p091_2(50, 50))
