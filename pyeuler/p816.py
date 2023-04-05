#!/usr/bin/env pypy3

def p816(N):

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance(self, p, r=2):
            if r == 0:
                return p.x - self.x
            elif r == 1:
                return p.y - self.y
            else:
                return ((self.x - p.x)**2 + (self.y - p.y)**2) ** .5

    class bbs:
        def __init__(self, value, mod):
            self.value = value
            self.mod   = mod

        def current(self):
            return self.value

        def next(self):
            self.value = pow(self.value, 2, self.mod)
            return self.value

    s      = bbs(290797, 50515093)
    P      = [Point(s.current(), s.next())]
    while len(P) < N:
        P  += [Point(s.next(), s.next())]

    P   = sorted(P, key=lambda p: p.x)
    res = P[0].distance(P[1])
    for i in range(len(P)):
        for j in range(i+1, len(P)):
            if P[i].distance(P[j], 0) >= res: break
            res = min(res, P[i].distance(P[j]))
    return round(res, 9)

print(p816(2_000_000))
